
class Contacthelper:
    def __init__(self,app):
        self.app=app

    def addnew(self, contact1):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact1)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, contact1):
        wd=self.app.wd
        self.change_field_value("firstname",contact1.fname)
        self.change_field_value("middlename", contact1.mname)
        self.change_field_value("lastname", contact1.lname)
        self.change_field_value("nickname", contact1.nname)
        self.change_field_value("title", contact1.title)
        self.change_field_value("company", contact1.compname)
        self.change_field_value("address", contact1.address)
        self.change_field_value("home", contact1.hphone)
        self.change_field_value("mobile", contact1.mphone)
        self.change_field_value("work", contact1.wphone)
        self.change_field_value("fax", contact1.faxnumber)
        self.change_field_value("email", contact1.e_mail)
        self.change_field_value("email2", contact1.e_mail2)
        self.change_field_value("email3", contact1.e_mail3)
        #wd.find_element_by_name("theform").click()
        self.change_field_value("homepage", contact1.home_page)
        #wd.find_element_by_name("theform").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[19]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[19]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[12]").click()
        self.change_field_value("byear", contact1.birth_year)
        #wd.find_element_by_name("theform").click()
        self.change_field_value("address2", contact1.address_2)
        self.change_field_value("notes", contact1.notes)
        wd.find_element_by_id("content").click()

    def change_field_value(self,field_name,text):
        wd=self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_first_contact(self):
        wd = self.app.wd

        #delet first contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("input[type=button][value=Delete]").click()
        wd.switch_to_alert().accept()

    def edit_first_contact(self,Contact1):
        wd=self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("img[alt=Edit]").click()
        self.fill_contact_form(Contact1)
        wd.find_element_by_name("update").click()