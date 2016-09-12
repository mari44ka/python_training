
import pytest
from fixture.Application import Application

fixture=None

@pytest.fixture()
def app(request):
    global fixture
    if fixture is None:
        fixture=Application()

    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.sessio.ensure_login(name="admin", password="secret")
    return fixture

@pytest.fixture(scope="session",autouse=True)  #fixture will play automaticly after using autouse
def stop(request):

    def fin():
        fixture.sessio.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

