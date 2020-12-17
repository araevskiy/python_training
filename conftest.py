

import pytest
from fixture.application import Application
from fixture.application2 import Application2



@pytest.fixture
def app(request):
     fixture = Application ()
     request.addfinalizer(fixture.destroy)
     return fixture

@pytest.fixture
def app2(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture
