# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
        app.open_homepage()
        app.sessio.login(name="admin", password="secret")
        app.group.creat(Group(name="my", footer="my", header="my"))
        app.sessio.logout()

def test_add_group_empty(app):
        app.open_homepage()
        app.sessio.login(name="admin", password="secret")
        app.group.creat(Group(name="", footer="", header=""))
        app.sessio.logout()
