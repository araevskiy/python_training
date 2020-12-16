# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contacts(app):
        app.login(usermane="admin", password="secret")
        app.create_contact(Contact(firstname="Aleу", secondname="RY"))
        app.logout()

def test_add_contacts2(app):
        app.login(usermane="admin", password="secret")
        app.create_contact(Contact(firstname="Anton", secondname="Matros"))
        app.logout()

