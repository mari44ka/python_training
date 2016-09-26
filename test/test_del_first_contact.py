from model.contact1 import Contact1

def test_del_first_contact(app):
    #app.open_homepage()
    old_contact=app.contact.get_contact_list()
    if app.contact.count()==0:
        app.contact.addnew(Contact1(fname="Helen", mname="Chao", lname="Chi",mphone="3435475", wphone="12345", e_mail="" ))
    app.contact.del_first_contact()
    new_contact=app.contact.get_contact_list()
    assert len(old_contact)-1==len(new_contact)
    old_contact[0:1]=[]
    assert old_contact==new_contact




