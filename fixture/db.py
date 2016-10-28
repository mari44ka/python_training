import pymysql
from model.group import Group
from model.contact1 import Contact1

class Dbfixture:
    def __init__(self,host,name,user,password):
        self.host=host
        self.name=name
        self.user=user
        self.password=password
        self.connection=pymysql.connect(host=host,database=name,user=user,password=password)
        self.connection.autocommit(True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id,group_name,group_header,group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id,firstname,middlename,lastname,nickname,company,title,address,home,mobile,work,fax,email,email2,email3,homepage,byear,address2,phone2,notes from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id,fname,mname,lname,nname,compname,title,address,hphone,mphone,wphone,faxnumber,e_mail,e_mail2,e_mail3,home_page,birth_year,address_2,secondphone,notes) = row
                list.append(Contact1(id=str(id),fname=fname, mname=mname, lname=lname, nname=nname, compname=compname, title=title, address=address,
                 hphone=hphone, mphone=mphone, wphone=wphone, faxnumber=faxnumber, e_mail=e_mail, e_mail2=e_mail2, e_mail3=e_mail3,
                 home_page=home_page,birth_year=str(birth_year), address_2=address_2, notes=notes,secondphone=secondphone))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()