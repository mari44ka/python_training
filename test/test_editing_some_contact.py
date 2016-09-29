from model.contact1 import Contact1
from random import randrange

def test_edit_some_contact(app):
    #app.open_homepage()
    if app.contact.count()==0:
        app.contact.addnew(Contact1(fname="Helen", mname="Chao", lname="Chi",mphone="3435475", wphone="12345", e_mail="" ))
    old_contact=app.contact.get_contact_list()
    index=randrange(len(old_contact))
    contact=Contact1(lname="Lo", hphone="7777",e_mail2="KK@mail.ru",notes="check")
    contact.id=old_contact[index].id
    app.contact.edit_contact_by_index(index,contact)
    new_contact=app.contact.get_contact_list()
    assert len(old_contact)==len(new_contact)
    old_contact[index]=contact
    assert sorted(old_contact,key=Contact1.id_or_max) == sorted(new_contact,key=Contact1.id_or_max)
