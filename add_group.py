# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group
import  unittest
from Application import Application


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class add_group(unittest.TestCase):
    def setUp(self):
        self.app=Application()

    def test_add_group(self):
        self.app.open_homepage()
        self.app.login(name="admin", password="secret")
        #creating group
        self.app.group_creating(Group(name="my", footer="my", header="my"))
        self.app.logout()

    def test_add_group_empty(self):

        self.app.open_homepage()
        self.app.login(name="admin", password="secret")

            # creating group
        self.app.group_creating(Group(name="", footer="", header=""))

        self.app.logout()


    def tearDown(self):
        self.app.destroy()


if __name__ == '__main__':
    unittest.main()