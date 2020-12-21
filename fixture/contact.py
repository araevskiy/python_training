class ContactHelper:

    def __init__(self, app):
        self.app= app

    def create(self, contact):
        wd = self.app.wd
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
        self.return_to_homepage()


    def delete_first_contact(self):
        wd = self.app.wd
        # select contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()


    def return_to_homepage(self):
        wd = self.app.wd
        # return to homepage
        wd.find_element_by_link_text("home page").click()




