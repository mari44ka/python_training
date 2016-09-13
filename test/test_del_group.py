
from model.group import Group

def test_del_first_group(app):
    if app.group.count()==0:
        app.group.creat(Group(name="Test1"))
    app.group.del_first_group()
