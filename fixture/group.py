

class Grouphelper:
    def __init__(self,app):
        self.app=app

    def creat(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        self.feel_group_form(group)
        wd.find_element_by_name("submit").click()

    def feel_group_form(self, group):
        wd=self.app.wd
        self.change_field_value("group_name",group.name)
        self.change_field_value("group_footer", group.footer)
        self.change_field_value("group_header", group.header)




    def change_field_value(self,field_name,text):
        wd=self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)



    def del_first_group(self):
        wd=self.app.wd
        self.app.open_homepage()
        wd.find_element_by_link_text("groups").click()
        # select first group
        self.select_first_group()
        #delete first group
        wd.find_element_by_name("delete").click()

    def select_first_group(self):
        wd=self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_group(self,new_group_data):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_link_text("groups").click()
        # select first group
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.feel_group_form(new_group_data)
        wd.find_element_by_name("update").click()

