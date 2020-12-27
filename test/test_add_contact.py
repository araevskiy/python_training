# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contacts(app):
        app.contact.create(Contact(firstname="Aleу", secondname="RY"))


def test_add_contacts2(app):
        app.contact.create(Contact(firstname="Anton", secondname="Matros"))


