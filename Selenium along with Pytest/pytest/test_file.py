import pytest

def test_case():
    print("hello world")

#markers
@pytest.mark.xfail
@pytest.mark.sanity
def test_case2():
    var="bhavani"
    assert var == "bhavani"
    print("its test")
#
class Test_file:
    def test_data1(self,data):
        print(data[0])
        
#Fixtures
@pytest.fixture(params=[1, 2, 3])
def my_fixture(param):
    return param

def test_my_fixture(my_fixture):
    assert my_fixture in [1, 2, 3]

@pytest.mark.parametrize("param", [1, 2, 3])
def test_my_fixture(param):
    assert param in [1, 2, 3]






