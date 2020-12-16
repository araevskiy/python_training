

class Session2Helper:

    def __init__(self, app2):
        self.app2 = app2

    def login(self, usermane, password):
        wd = self.app2.wd
        self.app2.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(usermane)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app2.wd
        # logout
        wd.find_element_by_link_text("Logout").click()