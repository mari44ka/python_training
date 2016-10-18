# -*- coding: utf-8 -*-

import string
import pytest
import random

from model.contact1 import Contact1

def random_string(prefix,maxlen):
    symbols=string.ascii_letters + string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata =[Contact1(fname="",mname="",lname="",nname="",title="",compname="",
           address="",hphone="",mphone="",wphone="",faxnumber="",secondphone="",
           e_mail="",e_mail2="",e_mail3="",home_page="",birth_year="",address_2="",notes="")] + [
    Contact1(fname=random_string("fname",10),mname=random_string("mname",10),lname=random_string("lname",15),
             nname=random_string("nname",5),title=random_string("title",4),compname=random_string("compname",10),
           address=random_string("address",20),hphone=random_string("hphone",10),mphone=random_string("mphone",10),
             wphone=random_string("wphone",10),faxnumber=random_string("faxnumber",10),secondphone=random_string("secondphone",10),
           e_mail=random_string("e_mail",20),e_mail2=random_string("e_mail2",20),e_mail3=random_string("e_mail3",20),
             home_page=random_string("home_page",22),birth_year=random_string("birth_year",4),
             address_2=random_string("address_2",20),notes=random_string("notes",25))
    for i in range(5)

]
@pytest.mark.parametrize("contact1",testdata,ids=[repr(x) for x in testdata])
    
def test_add_new_contact(app,contact1):
    old_contact = app.contact.get_contact_list()
    app.contact.addnew(contact1)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact1)
    assert sorted(old_contact,key=Contact1.id_or_max)==sorted(new_contact,key=Contact1.id_or_max)





