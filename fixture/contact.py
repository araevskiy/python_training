from selenium.webdriver.support.select import Select
from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.contact import Contact
import re
from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_element_by_link_text("Last name")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        # init new contact
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_homepage()
        self.contact_cache = None

    def fill_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.secondname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("address", contact.address)
        self.change_field_value("address2", contact.secondaddress)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_for_edit_by_id(id)
        # fill contact form
        self.fill_form(new_contact_data)
        # submit contact update
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def add_contact_in_group_by_id(self, id_contact, id_group):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id_contact).click()
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_xpath("//select[@name='to_group']")).select_by_value(id_group)
        wd.find_element_by_name("add").click()
        self.contact_cache = None

    def del_contact_from_group_by_id(self, id_contact, id_group):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_xpath("//select[@name='group']")).select_by_value(id_group)
        wd.find_element_by_css_selector("input[value='%s']" % id_contact).click()
        wd.find_element_by_name("remove").click()
        self.contact_cache = None

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_for_edit_by_index(index)
        self.fill_form(contact)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def open_contact_for_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_for_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("a[href='edit.php?id=" + str(id) + "']").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("(// img[@ alt='Details'])[" + str(index + 1) + "]").click()

    def open_contact_for_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def select_none(self):
        wd = self.app.wd
        self.app.open_home_page()
        Select(wd.find_element_by_name("group")).select_by_visible_text("[none]")
        wd.find_element_by_xpath("//option[@value='[none]']").click()


    def return_to_homepage(self):
        wd = self.app.wd
        # return to homepage
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("MainForm")) > 0):
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def count_contacts_in_group(self):
        wd = self.app.wd
        self.return_to_homepage()
        self.select_none()
        return len(wd.find_elements_by_name("selected[]"))

    def count_contacts_not_in_group(self):
        wd = self.app.wd
        self.return_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            wd.find_element_by_name("group").click()
            Select(wd.find_element_by_name("group")).select_by_visible_text("[all]")
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = row.find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_for_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        secondaddress = wd.find_element_by_name("address2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address,secondaddress=secondaddress,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone,
                       email=email, email2=email2, email3=email3)

    @staticmethod
    def search_in_text(search_text, text):
        search_result = re.search(search_text, text)
        if search_result is not None:
            return search_result.group(1)
        else:
            return ''

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = self.search_in_text("H: (.*)", text)
        workphone = self.search_in_text("W: (.*)", text)
        mobilephone = self.search_in_text("M: (.*)", text)
        secondaryphone = self.search_in_text("P: (.*)", text)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                       secondaryphone=secondaryphone)










