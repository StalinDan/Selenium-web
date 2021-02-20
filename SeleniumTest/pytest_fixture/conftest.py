import pytest


@pytest.fixture(scope='function')
def all_fixture(request):
    print('全局前置的方法')
    # return和yield都表示返回的意思，但是return后面不能有代码，yield返回后，后面可以有代码
    yield request
    print('全局后置的方法')