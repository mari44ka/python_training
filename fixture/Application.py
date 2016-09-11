
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.sessio import Sessionhelper
from fixture.group import Grouphelper
from fixture.contact import Contacthelper

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.sessio=Sessionhelper(self)
        self.group=Grouphelper(self)
        self.contact=Contacthelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_homepage(self):
        wd=self.wd
        wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()

