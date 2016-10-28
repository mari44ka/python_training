
from model.group import Group
import random

def test_some_first_group(app,db,check_ui):
    if len(db.get_group_list())==0:
        db.creat(Group(name="Test1",footer="Test2"))
    old_groups = db.get_group_list()
    group=random.choice(old_groups)
    modify_group=Group(name="Hallo")
    modify_group.id=group.id
    app.group.edit_group_by_id(group.id,modify_group)
    new_groups = db.get_group_list()
    assert len(old_groups)== len(new_groups)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)





