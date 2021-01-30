from model.contact import Contact
from random import randrange




def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="11", secondname="22",lastname="gg",))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="A8888l6", secondname="Rs88", lastname="81", homephone="33333", mobilephone="2222",
                      workphone="1111", secondaryphone="555555", email="aeg5@mail.ru", email2="123592@mail.ru",
                      email3="sasha1992@mail.ru", address="LasVegas")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


