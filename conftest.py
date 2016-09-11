
import pytest
from fixture.Application import Application



@pytest.fixture(scope="session")
def app(request):
    fixture=Application()
    fixture.sessio.login(name="admin", password="secret")
    def fin():
        fixture.sessio.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

