from model.contact1 import Contact1

def test_edit_first_contact(app):
    app.open_homepage()
    app.contact.edit_first_contact(Contact1(lname="Lo", hphone="7777",e_mail2="KK@mail.ru",notes="check"))

