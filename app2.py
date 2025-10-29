# practice pytest
import pytest


class Test1:

    @pytest.mark.parametrize("geometry", ["test1", "test2", "test3"])
    def test_method1(self, geometry):
        print("geometry called is -- {}".format(geometry))
