from model.contact1 import Contact11

def test_edit_first_contact(app):
    app.open_homepage()
    app.sessio.login(name="admin", password="secret")
    app.contact.edit_first_contact(Contact11(lname="Lo", hphone="7777",e_mail2="KK@mail.ru"))
    app.sessio.logout()
