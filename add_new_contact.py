# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver

import  unittest
from contact1 import Contact1
from Contactapp import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add_new_contact(unittest.TestCase):
    def setUp(self):
        self.app=Contact()
    
    def test_add_new_contact(self):
        self.app.open_homepage()
        self.app.login(name="admin", password="secret")
        self.app.addnew_contact(Contact1(fname="Marta", mname="Vu", lname="Ko", nname="no", title="no", compname="Google",
                            address="no", hphone="9999", mphone="4444", wphone="6666", faxnumber="no",
                            e_mail="ya@gmail.com", e_mail2="no", e_mail3="no", home_page="no", birth_year="1980",
                            address_2="no", notes="no"))
        self.app.logout()


    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
