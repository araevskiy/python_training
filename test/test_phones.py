from model.contact import Contact
import re


def test_contact_on_home_page_and_edit(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_and_edit_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.id == contact_from_edit_page.id


def test_contact_on_home_page_and_db(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    list_contacts_from_home_page = list(
        map(lambda i: (i.identifier, i.firstname, i.lastname, i.all_phones_from_home_page, i.all_email_from_home_page,
                       i.address_company), contacts_from_home_page))
    list_contacts_from_db = list(
        map(lambda i: (i.identifier, i.firstname, i.lastname, merge_phones_like_on_home_page(i),
                       merge_emails_like_on_home_and_edit_page(i), i.address_company), contacts_from_db))
    assert sorted(list_contacts_from_home_page, key=lambda i: i[0]) == sorted(list_contacts_from_db, key=lambda i: i[0])


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))


def merge_emails_like_on_home_and_edit_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None, [contact.email, contact.email2, contact.email3]))