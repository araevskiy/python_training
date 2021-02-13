from model.contact import Contact
from model.group import Group
import random
import allure


def test_add_contact_in_group(app, orm, check_ui):
    with allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
        app.contact.create(Contact(firstname="A8888l6", secondname="Rs88", lastname="81", homephone="33333", mobilephone="2222",
                      workphone="1111", secondaryphone="555555", email="aeg5@mail.ru", email2="123592@mail.ru",
                      email3="sasha1992@mail.ru", address="LasVegas"))
        contacts = orm.get_contact_list()
        with allure.step('Given a non-empty group list'):
            if app.group.count() == 0:
                app.group.create(Group(name='Test'))
            groups = orm.get_group_list()
        if orm.all_contacts_in_all_groups(groups):
            app.group.create(Group(name='Test'))
    with allure.step('Given a random contact from the list'):
        edit_contact = random.choice(contacts)
    with allure.step('Given a random group from the list'):
        add_group_to_contact = random.choice(groups)
    with allure.step('When I add contact %s in group %s from the list' % (edit_contact, add_group_to_contact)):
        app.contact.add_contact_in_group_by_id(edit_contact.identifier, add_group_to_contact.identifier)
    with allure.step('Then the edited contact will be in the contact list of the selected group'):
        new_contacts = orm.get_contact_list()
        list_contacts_in_group = orm.contacts_in_group(add_group_to_contact)
        assert edit_contact in list_contacts_in_group
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
