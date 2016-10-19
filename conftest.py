
import pytest
from fixture.Application import Application

fixture=None

@pytest.fixture()
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    if fixture is None:

        fixture=Application(browser=browser,base_url=base_url)

    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser,base_url=base_url)
    fixture.sessio.ensure_login(name="admin", password="secret")
    return fixture

@pytest.fixture(scope="session",autouse=True)  #fixture will play automaticly after using autouse
def stop(request):

    def fin():
        fixture.sessio.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="firefox")
    parser.addoption("--base_url",action="store",default="http://localhost/addressbook/index.php")