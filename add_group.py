# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver

import  unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_group(self):

        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, name="admin", password="secret")

        #creating group
        self.group_creating(wd, name="my", footer="my", header="my")

        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def group_creating(self, wd, name, footer, header):
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("submit").click()

    def login(self, wd, name, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_css_selector("html").click()
        wd.find_element_by_css_selector("html").click()

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()