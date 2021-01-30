from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, orm, check_ui):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="A8888l6", secondname="Rs88", lastname="81", homephone="33333", mobilephone="2222",
                    workphone="1111", secondaryphone="555555", email="aeg5@mail.ru", email2="123592@mail.ru",
                    email3="sasha1992@mail.ru", address="LasVegas"))
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    contacts = orm.get_contact_list()
    groups = orm.get_group_list()
    edit_contact = random.choice(contacts)
    del_group_from_contact = random.choice(groups)
    if len(orm.contacts_in_group(del_group_from_contact)) == 0:
        app.contact.add_contact_in_group_by_id(edit_contact.id, del_group_from_contact.id)
    app.contact.del_contact_from_group_by_id(edit_contact.id, del_group_from_contact.id)
    new_contacts = orm.get_contact_list()
    list_contacts_not_in_group = orm.contacts_not_in_group(del_group_from_contact)
    assert edit_contact in list_contacts_not_in_group
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)