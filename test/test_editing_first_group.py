
from model.group import Group

def test_edit_first_group(app):
    app.open_homepage()
    app.group.edit_first_group(Group(name="Hallo"))




