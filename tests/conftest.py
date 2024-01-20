import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome_docker", help="Type in browser type")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def driver_fixture(browser):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = 'eager'  # 'normal' probably will work with chrome 114
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--log-level=3')

    if browser == "chrome_local":
        chrome_driver_path = ChromeDriverManager().install()
        service = Service(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    elif browser == "chrome_docker":
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=chrome_options)
    else:
        raise Exception(f'"{browser}" is not a supported browser')

    driver.implicitly_wait(1)
    yield driver
    driver.quit()
