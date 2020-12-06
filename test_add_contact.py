# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact


class TestAddContacts(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, usermane, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(usermane)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def create_contact(self, wd, contact):
        # init new contact
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.secondname)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_homepage(self, wd):
        # return to homepage
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def test_add_contacts(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, usermane="admin", password="secret")
        self.create_contact(wd, Contact(firstname="Aleу", secondname="RY"))
        self.return_to_homepage(wd)
        self.logout(wd)

    def test_add_contacts2(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, usermane="admin", password="secret")
        self.create_contact(wd, Contact(firstname="Anton", secondname="Matros"))
        self.return_to_homepage(wd)
        self.logout(wd)

    def tearDown(self):
            self.wd.quit()

if __name__ == "__main__":
        unittest.main()
