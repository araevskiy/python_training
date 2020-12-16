# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application2 import Application2

@pytest.fixture
def app2(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contacts(app2):
        app2.session2.login(usermane="admin", password="secret")
        app2.contact.create_contact(Contact(firstname="Aleу", secondname="RY"))
        app2.session2.logout()

def test_add_contacts2(app2):
        app2.session2.login(usermane="admin", password="secret")
        app2.contact.create_contact(Contact(firstname="Anton", secondname="Matros"))
        app2.session2.logout()

