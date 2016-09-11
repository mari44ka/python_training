# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
        app.open_homepage()
        app.group.creat(Group(name="my", footer="my", header="my"))


def test_add_group_empty(app):
        app.open_homepage()
        app.group.creat(Group(name="", footer="", header=""))

