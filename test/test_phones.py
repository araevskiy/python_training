from model.contact import Contact
import re
from random import randrange


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Anton", secondname="denisovish", lastname="gg",
                                   homephone="8000", mobilephone="3434434", workphone="444444", address="Moscow",
                                   secondaryphone="9090909", email="gennady@mail.ru", email2="dmitry@mail.ru", email3="Sasha@mail.ru"))
    list_contacts = app.contact.get_contact_list()
    index = randrange(len(list_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_from_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_from_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Anton", secondname="denisovish", lastname="gg",
                                   homephone="8000", mobilephone="3434434", workphone="444444", address="Moscow",
                                   secondaryphone="9090909", email="gennady@mail.ru", email2="dmitry@mail.ru",
                                   email3="Sasha@mail.ru"))
    list_contacts = app.contact.get_contact_list()
    index = randrange(len(list_contacts))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[./() -]", "", s)


def merge_phones_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None, [contact.email, contact.email2, contact.email3]))