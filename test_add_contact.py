# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import pytest
from contact import Contact
from application import Application

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

