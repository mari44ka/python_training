import re

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
        self.change_field_value("phone2", contact1.secondphone)
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
                all_phones=cells[5].text.splitlines()
                address=cells[3].text
                all_emails=cells[4].text.splitlines()
                self.contact_cache.append(Contact1(id=id, fname=fname, lname=lname, hphone=all_phones[0],e_mail3=all_emails[2],
                    mphone=all_phones[1],wphone=all_phones[2],secondphone=all_phones[3],address=address,e_mail=all_emails[0],e_mail2=all_emails[1]))

        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self,index):
        wd=self.app.wd
        self.app.open_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self,index):
        wd = self.app.wd
        self.app.open_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self,index):
        wd=self.app.wd
        self.open_contact_to_edit_by_index(index)
        fname= wd.find_element_by_name("firstname").get_attribute("value")
        lname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        hphone=wd.find_element_by_name("home").get_attribute("value")
        mphone = wd.find_element_by_name("mobile").get_attribute("value")
        wphone = wd.find_element_by_name("work").get_attribute("value")
        secondphone = wd.find_element_by_name("phone2").get_attribute("value")
        address=wd.find_element_by_name("address").get_attribute("value")
        e_mail=wd.find_element_by_name("email").get_attribute("value")
        e_mail2=wd.find_element_by_name("email2").get_attribute("value")
        e_mail3=wd.find_element_by_name("email3").get_attribute("value")
        return Contact1(fname=fname,lname=lname,id=id,hphone=hphone,mphone=mphone,wphone=wphone,
                        secondphone=secondphone,address=address,e_mail=e_mail,e_mail2=e_mail2,e_mail3=e_mail3)

    def get_contact_from_view_page(self,index):
        wd=self.app.wd
        self.open_contact_view_by_index(index)
        text=wd.find_element_by_id("content").text
        hphone=re.search("H: (.*)",text).group(1)
        mphone = re.search("M: (.*)", text).group(1)
        wphone = re.search("W: (.*)", text).group(1)
        secondphone = re.search("P: (.*)", text).group(1)
        return Contact1(hphone=hphone, mphone=mphone, wphone=wphone,
                    secondphone=secondphone)