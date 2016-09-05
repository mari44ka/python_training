# -*- coding: utf-8 -*-
import pytest

from fixture.Application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_group(app):
        app.open_homepage()
        app.sessio.login(name="admin", password="secret")
        app.group_creating(Group(name="my", footer="my", header="my"))
        app.sessio.logout()

def test_add_group_empty(app):
        app.open_homepage()
        app.sessio.login(name="admin", password="secret")
        app.group_creating(Group(name="", footer="", header=""))
        app.sessio.logout()





