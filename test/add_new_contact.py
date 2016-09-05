# -*- coding: utf-8 -*-


import pytest

from fixture.Contactapp import Contact
from model.contact1 import Contact1


@pytest.fixture
def kpp(request):
    fixture=Contact()
    request.addfinalizer(fixture.destroy)
    return fixture


    
def test_add_new_contact(kpp):
    kpp.open_homepage()
    kpp.sessio.login(name="admin", password="secret")
    kpp.contact.addnew(Contact1(fname="Marta", mname="Vu", lname="Ko", nname="no", title="no", compname="Google",
                        address="no", hphone="9999", mphone="4444", wphone="6666", faxnumber="no",
                        e_mail="ya@gmail.com", e_mail2="no", e_mail3="no", home_page="no", birth_year="1980",
                        address_2="no", notes="no"))
    kpp.sessio.logout()



