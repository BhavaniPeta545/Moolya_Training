import pytest
from conftest import setup

@pytest.mark.usefixtures("setup")
class Test_class:
    def test_case3(self):
        a=2
        b=3
        print(a+b)

    def test_case4(self):
        print("hello bhavani")
# a=C1()
# a.test_case3()
# a.test_case4()