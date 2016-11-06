# -*- coding: utf-8 -*-





from model.contact1 import Contact1



    
def test_add_new_contact(app,db,json_contacts,check_ui):
    contact1=json_contacts
    old_contact = db.get_contact_list()
    app.contact.addnew(contact1)
    new_contact = db.get_contact_list()
    old_contact.append(contact1)
    assert sorted(old_contact, key=Contact1.id_or_max) == sorted(new_contact, key=Contact1.id_or_max)
    if check_ui:
        assert sorted(old_contact,key=Contact1.id_or_max) == sorted(new_contact,key=Contact1.id_or_max)





