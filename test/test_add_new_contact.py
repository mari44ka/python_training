# -*- coding: utf-8 -*-



from model.contact1 import Contact1
    
def test_add_new_contact(app):
    old_contact = app.contact.get_contact_list()
    contact=Contact1(fname="Marta", mname="Vu",lname="Ko", nname="no", title="no", compname="Google",
                        address="no", hphone=" ", mphone="4444", wphone="6666", faxnumber="no",secondphone="345",
                        e_mail=" ", e_mail2=" ", e_mail3="no", home_page="no", birth_year="1980",
                        address_2="no", notes="no")
    app.contact.addnew(contact)
    assert len(old_contact) + 1==app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact,key=Contact1.id_or_max)==sorted(new_contact,key=Contact1.id_or_max)





