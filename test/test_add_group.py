# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
        app.open_homepage()
        old_groups=app.group.get_group_list()
        app.group.creat(Group(name="my", footer="my", header="my"))
        new_groups=app.group.get_group_list()
        assert len(old_groups)+1==len(new_groups)


def test_add_group_empty(app):
        app.open_homepage()
        old_groups = app.group.get_group_list()
        app.group.creat(Group(name="", footer="", header=""))
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)


