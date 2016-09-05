from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.sessio import Sessionhelper
from fixture.contact import Contacthelper
class Contact:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.sessio = Sessionhelper(self)
        self.contact=Contacthelper(self)


    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")


    def destroy(self):
        self.wd.quit()