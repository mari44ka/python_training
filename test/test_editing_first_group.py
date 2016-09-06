
from model.group import Group

def test_edit_first_group(app):
    app.open_homepage()
    app.sessio.login(name="admin", password="secret")
    app.group.edit_first_group(Group(name="ok", footer="ok", header="ok"))
    app.sessio.logout()

