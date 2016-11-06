from model.contact1 import Contact1
import random

def test_del_some_contact(app,db,check_ui):
    if len(db.get_contact_list())==0:
        app.contact.addnew(Contact1(fname="Helen", mname="Chao", lname="Chi",mphone="3435475", wphone="12345", e_mail="" ))
    old_contact = db.get_contact_list()
    contact=random.choice(old_contact)
    app.contact.del_contact_by_id(contact.id)
    new_contact=db.get_contact_list()
    #assert len(old_contact)-1 == len(new_contact)
    old_contact.remove(contact)
    assert old_contact==new_contact
    if check_ui:
        assert sorted(new_contact,key=Contact1.id_or_max)==sorted(app.contact.get_contact_list(),key=Contact1.id_or_max)

