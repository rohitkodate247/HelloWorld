# practice pytest

import pytest


class Test1:

    @pytest.fixture(scope='class', autouse=True)
    def myfixture(self, request):
        print("my fixture is called")

        def teardown():
            print("teardown method is called")
        request.addfinalizer(teardown)

    def test_method1(self):
        print("method-1 is called")

    def test_method2(self):
        print("method-2 is called")
