from model.contact1 import Contact1
import random

def test_edit_some_contact(app,db,check_ui):
    if len(db.get_contact_list())==0:
        app.contact.addnew(Contact1(fname="Helen", mname="Chao", lname="Chi",mphone="3435475", wphone="12345",secondphone="567", e_mail="tt@ru.com" ))
    old_contact=db.get_contact_list()
    contact=random.choice(old_contact)
    modify_contact=Contact1(fname="Janny",lname="Lost")
    modify_contact.id=contact.id
    app.contact.edit_contact_by_id(contact.id,modify_contact)
    new_contact=db.get_contact_list()
    assert len(old_contact)==len(new_contact)
    if check_ui:
        assert sorted(old_contact,key=Contact1.id_or_max) == sorted(new_contact,key=Contact1.id_or_max)
