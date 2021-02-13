from model.contact import Contact
from model.group import Group
import random
import allure


def test_del_contact_from_group(app, orm, check_ui):
    with allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
           app.contact.create(
            Contact(firstname="A8888l6", secondname="Rs88", lastname="81", homephone="33333", mobilephone="2222",
                    workphone="1111", secondaryphone="555555", email="aeg5@mail.ru", email2="123592@mail.ru",
                    email3="sasha1992@mail.ru", address="LasVegas"))
    contacts = orm.get_contact_list()
    with allure.step('Given a non-empty group list'):
        if app.group.count() == 0:
            app.group.create(Group(name='Test'))
        groups = orm.get_group_list()
    with allure.step('Given a random contact from the list'):
        edit_contact = random.choice(contacts)
    with allure.step('Given a random group from the list'):
        del_group_from_contact = random.choice(groups)
    if len(orm.contacts_in_group(del_group_from_contact)) == 0:
        app.contact.add_contact_in_group_by_id(edit_contact.id, del_group_from_contact.id)
    with allure.step('When I delete contact %s in group %s from the list' % (edit_contact, del_group_from_contact)):
        app.contact.del_contact_from_group_by_id(edit_contact.id, del_group_from_contact.id)
    with allure.step('Then the edited contact will not be in the contact list of the selected group'):
        new_contacts = orm.get_contact_list()
        list_contacts_not_in_group = orm.contacts_not_in_group(del_group_from_contact)
        assert edit_contact in list_contacts_not_in_group
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)