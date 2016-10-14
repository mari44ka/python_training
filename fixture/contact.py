from model.contact1 import Contact1
class Contacthelper:
    def __init__(self,app):
        self.app=app

    def addnew(self, contact1):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact1)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache =None

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
        self.del_contact_by_index(0)


    def del_contact_by_index(self,index):
        wd = self.app.wd
        #delet first contact
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_css_selector("input[type=button][value=Delete]").click()
        wd.switch_to_alert().accept()
        self.contact_cache=None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self,index,Contact1):
        wd=self.app.wd
        row=wd.find_elements_by_name("entry")[index]
        cell=row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_css_selector('img[alt="Edit"]').click()
        self.fill_contact_form(Contact1)
        wd.find_element_by_name("update").click()
        self.contact_cache=None


    def count(self):
        wd=self.app.wd
        self.app.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))


    contact_cache=None


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_homepage()
            self.contact_cache= []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                fname = cells[2].text
                lname = cells[1].text
                self.contact_cache.append(Contact1(id=id, fname=fname, lname=lname))

        return list(self.contact_cache)

