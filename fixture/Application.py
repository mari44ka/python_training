
from selenium.webdriver.firefox.webdriver import WebDriver

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def logout(self):
        wd=self.wd
        wd.find_element_by_link_text("Logout").click()

    def group_creating(self,group):
        wd=self.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("submit").click()



    def login(self,name, password):

        # login
        wd=self.wd
        self.open_homepage()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_css_selector("html").click()
        wd.find_element_by_css_selector("html").click()

    def open_homepage(self):
        wd=self.wd
        wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()

