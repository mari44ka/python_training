from model.contact1 import Contact1
from random import randrange

def test_edit_some_contact(app):
    #app.open_homepage()
    if app.contact.count()==0:
        app.contact.addnew(Contact1(fname="Helen", mname="Chao", lname="Chi",mphone="3435475", wphone="12345",secondphone="567", e_mail="tt@ru.com" ))
    old_contact=app.contact.get_contact_list()
    index=randrange(len(old_contact))
    contact=Contact1(lname="Lo",fname="Linda", hphone="7777",e_mail2="KK@mail.ru",notes="check",secondphone="0000")
    contact.id=old_contact[index].id
    app.contact.edit_contact_by_index(index,contact)
    new_contact=app.contact.get_contact_list()
    assert len(old_contact)==len(new_contact)
    old_contact[index]=contact
    assert sorted(old_contact,key=Contact1.id_or_max) == sorted(new_contact,key=Contact1.id_or_max)
