# -*- coding: utf-8 -*-

from model.group import Group
import pytest
import random
import string

def random_string(prefix,maxlen):
    symbols=string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata =[ Group(name="", footer="", header="")]+[
            Group(name=random_string("name",10), footer=random_string("footer",20), header=random_string("header",15))
        for i in range(5)

        ]
@pytest.mark.parametrize("group",testdata,ids=[repr(x) for x in testdata])

def test_add_group(app,group):

        app.open_homepage()
        old_groups=app.group.get_group_list()
        app.group.creat(group)
        assert len(old_groups)+1==app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups,key=Group.id_or_max)==sorted(new_groups,key=Group.id_or_max)


#def test_add_group_empty(app):
        #app.open_homepage()
        #old_groups = app.group.get_group_list()
        #group=Group(name="", footer="", header="")
        #app.group.creat(group)
        #assert len(old_groups) + 1 ==app.group.count()
        #new_groups = app.group.get_group_list()
        #old_groups.append(group)
        #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


