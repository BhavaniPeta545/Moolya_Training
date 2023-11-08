import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class",params=["chrome","firefox"])
def setup(request):
    print("intializing driver")
    service_obj = Service()
    if request.param =="chrome":
        driver = webdriver.Chrome(service=service_obj)
        request.instance.driver = driver
        yield driver
        driver.quit()
    # elif request.param =="firefox":
    #     driver = webdriver.Firefox(service=service_obj)
    #     yield driver
    #     driver.quit()

    # if request.param =="MicrosoftEdge":
    #     driver = webdriver.Edge(service=service_obj)

    # driver=request.instance.driver
    # driver.maximize_window()


    # yield driver




# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @pytest.fixture()
# def browser(request):
#     print("initiating chrome driver")
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     request.instance.driver = driver
#     driver.maximize_window()
#
#     yield driver
#
#     driver.quit()


