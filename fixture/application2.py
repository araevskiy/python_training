from selenium import webdriver
from fixture.session2 import Session2Helper
from fixture.contact import ContactHelper

class Application2 :

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session2 = Session2Helper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
