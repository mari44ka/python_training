from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact1 import Contact1
from pymysql.converters import decoders
class Ormfixture:
    db = Database()

    class Ormgroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int,column="group_id")
        name=Optional(str,column="group_name")
        header=Optional(str,column="group_header")
        footer=Optional(str,column="group_footer")
        contacts=Set(lambda: Ormfixture.Ormcontact,table="address_in_groups",column="id",reverse="groups",lazy=True)


    class Ormcontact(db.Entity):
        _table_ = "addressbook"
        id=PrimaryKey(int,column="id")
        firstname=Optional(str,column="firstname")
        lastname=Optional(str,column="lastname")
        deprecated=Optional(datetime,column="deprecated")
        groups=Set(lambda: Ormfixture.Ormgroup,table="address_in_groups",column="group_id",reverse="contacts",lazy=True)


    def __init__(self,host,name,user,password):
        self.db.bind("mysql",host=host,database=name,user=user,password=password,conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)

        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact1(id=str(contact.id), fname=contact.firstname, lname=contact.lastname)

        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in Ormfixture.Ormgroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in Ormfixture.Ormcontact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in Ormfixture.Ormgroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in Ormfixture.Ormgroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in Ormfixture.Ormcontact if c.deprecated is None and orm_group not in c.groups))










