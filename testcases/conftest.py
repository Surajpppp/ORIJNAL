import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("launching chrome")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("launching firefox")
    else:
        driver = webdriver.Chrome()
        print("launching chrome")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'origalnalpractice'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'suraj'
#
#
# # It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
