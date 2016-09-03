# -*- coding: utf-8 -*-


import pytest
from contact1 import Contact1
from Contactapp import Contact


@pytest.fixture
def kpp(request):
    fixture=Contact()
    request.addfinalizer(fixture.destroy)
    return fixture


    
def test_add_new_contact(kpp):
    kpp.open_homepage()
    kpp.login(name="admin", password="secret")
    kpp.addnew_contact(Contact1(fname="Marta", mname="Vu", lname="Ko", nname="no", title="no", compname="Google",
                            address="no", hphone="9999", mphone="4444", wphone="6666", faxnumber="no",
                            e_mail="ya@gmail.com", e_mail2="no", e_mail3="no", home_page="no", birth_year="1980",
                            address_2="no", notes="no"))
    kpp.logout()



