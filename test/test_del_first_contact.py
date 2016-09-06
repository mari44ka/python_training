

def test_del_first_contact(app):
    app.open_homepage()
    app.sessio.login(name="admin", password="secret")
    app.contact.del_first_contact()
    app.sessio.logout()