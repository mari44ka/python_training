
from model.group import Group

def test_edit_first_group(app):
    if app.group.count()==0:
        app.group.creat(Group(name="Test1",footer="Test2"))
    app.group.edit_first_group(Group(name="Hallo"))




