# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
     fixture = Application ()
     request.addfinalizer(fixture.destroy)
     return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="fdfd", header="fdfdf", footer="fdfdff"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

