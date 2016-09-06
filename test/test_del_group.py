

def test_del_first_group(app):
    app.open_homepage()
    app.sessio.login(name="admin", password="secret")
    app.group.creat(Group(name="my", footer="my", header="my"))
    app.group.del_first_group()
    app.sessio.logout()