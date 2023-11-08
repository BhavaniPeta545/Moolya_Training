import pytest

@pytest.fixture(scope='function')
def setup():
    print("this is a setup session")
    yield
    print("this will execute last/teardown method")
#
# @pytest.fixture()
# def data():
#     return ["bhavani","hari"]
#
# @pytest.fixture(params=["app","aplication"])
# def options(params):
#     return params


@pytest.fixture(params=["chrome", "firefox", "MicrosoftEdge"],scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    if request.param == "MicrosoftEdge":
        web_driver = webdriver.Edge(executable_path=r'C:\EdgeDriver\MicrosoftWebDriver.exe')
    request.cls.driver = web_driver
    yield
    web_driver.close()

