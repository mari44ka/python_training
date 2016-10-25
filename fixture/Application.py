
from selenium import webdriver
from fixture.session import Sessionhelper
from fixture.group import Grouphelper
from fixture.contact import Contacthelper

class Application:
    def __init__(self,browser,base_url):
        if browser=="firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome("/Users/Mari/Downloads/chromedriver")
        elif browser == "safari":
            self.wd = webdriver.Safari("/usr/bin/safaridriver")
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        #self.wd.implicitly_wait(5) only for dynamic applications
        self.session=Sessionhelper(self)
        self.group=Grouphelper(self)
        self.contact=Contacthelper(self)
        self.base_url=base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_homepage(self):
        wd=self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

