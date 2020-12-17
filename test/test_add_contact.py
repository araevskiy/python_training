# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contacts(app2):
        app2.session2.login(usermane="admin", password="secret")
        app2.contact.create_contact(Contact(firstname="Aleу", secondname="RY"))
        app2.session2.logout()

def test_add_contacts2(app2):
        app2.session2.login(usermane="admin", password="secret")
        app2.contact.create_contact(Contact(firstname="Anton", secondname="Matros"))
        app2.session2.logout()

