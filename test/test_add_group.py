# -*- coding: utf-8 -*-

from model.group import Group
import pytest

testdata =[
            Group(name="my", footer="my", header="my"),
            Group(name="", footer="", header="")
        ]
@pytest.mark.parametrize("group",testdata,ids=[repr(x) for x in testdata])

def test_add_group(app,group):
        pass
        #app.open_homepage()
        #old_groups=app.group.get_group_list()
        #group=Group(name="my", footer="my", header="my")
        #app.group.creat(group)
        #assert len(old_groups)+1==app.group.count()
        #new_groups = app.group.get_group_list()
        #old_groups.append(group)
        #assert sorted(old_groups,key=Group.id_or_max)==sorted(new_groups,key=Group.id_or_max)


#def test_add_group_empty(app):
        #app.open_homepage()
        #old_groups = app.group.get_group_list()
        #group=Group(name="", footer="", header="")
        #app.group.creat(group)
        #assert len(old_groups) + 1 ==app.group.count()
        #new_groups = app.group.get_group_list()
        #old_groups.append(group)
        #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


