
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.sessio import Sessionhelper
from fixture.group import Grouphelper

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.sessio=Sessionhelper(self)
        self.group=Grouphelper(self)


    def open_homepage(self):
        wd=self.wd
        wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()

