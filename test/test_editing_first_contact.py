from model.contact1 import Contact1

def test_edit_first_contact(app):
    #app.open_homepage()
    if app.contact.count()==0:
        app.contact.addnew(Contact1(fname="Helen", mname="Chao", lname="Chi",mphone="3435475", wphone="12345", e_mail="" ))
    old_contact=app.contact.get_contact_list()
    cont=Contact1(lname="Lo", hphone="7777",e_mail2="KK@mail.ru",notes="check")
    cont.id=old_contact[0].id
    app.contact.edit_first_contact(cont)
    new_contact=app.contact.get_contact_list()
    assert len(old_contact)==len(new_contact)
    old_contact[0]=cont
    assert sorted(old_contact,key=Contact1.id_or_max) == sorted(new_contact,key=Contact1.id_or_max)
