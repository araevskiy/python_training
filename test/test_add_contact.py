# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contacts(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Aleу", secondname="RY")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contacts2(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Anton", secondname="Matros")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



