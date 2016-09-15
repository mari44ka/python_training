from model.contact1 import Contact1

def test_del_first_contact(app):
    app.open_homepage()
    if app.contact.count()==0:
        app.contact.addnew(Contact1(fname="Helen", mname="Chao", lname="Chi",mphone="3435475", wphone="12345", e_mail="" ))
    app.contact.del_first_contact()




