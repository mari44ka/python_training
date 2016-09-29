from model.contact1 import Contact1
from random import randrange

def test_del_some_contact(app):
    #app.open_homepage()
    old_contact=app.contact.get_contact_list()
    if app.contact.count()==0:
        app.contact.addnew(Contact1(fname="Helen", mname="Chao", lname="Chi",mphone="3435475", wphone="12345", e_mail="" ))
    index=randrange(len(old_contact))
    app.contact.del_contact_by_index(index)
    new_contact=app.contact.get_contact_list()
    assert len(old_contact)-1==len(new_contact)
    old_contact[index:index+1]=[]
    assert old_contact==new_contact




