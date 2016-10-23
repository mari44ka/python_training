# -*- coding: utf-8 -*-





from model.contact1 import Contact1


    
def test_add_new_contact(app,json_contacts):
    contact1=json_contacts
    old_contact = app.contact.get_contact_list()
    app.contact.addnew(contact1)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact1)
    assert sorted(old_contact,key=Contact1.id_or_max)==sorted(new_contact,key=Contact1.id_or_max)





