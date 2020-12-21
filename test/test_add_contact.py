# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contacts(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="Aleу", secondname="RY"))
        app.session.logout()

def test_add_contacts2(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="Anton", secondname="Matros"))
        app.session.logout()

