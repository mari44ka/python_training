from model.contact1 import Contact1

def test_edit_first_contact(app):
    app.open_homepage()
    if app.contact.count()==0:
        app.contact.addnew(Contact1(fname="Helen", mname="Chao", lname="Chi",mphone="3435475", wphone="12345", e_mail="" ))
    app.contact.edit_first_contact(Contact1(lname="Lo", hphone="7777",e_mail2="KK@mail.ru",notes="check"))

