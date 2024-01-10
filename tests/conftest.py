import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')

    # Use ChromeDriverManager to automatically download and ma
    # nage the ChromeDriver executable
    chrome_driver_path = ChromeDriverManager().install()

    # Create a Service instance with the path to the ChromeDriver executable
    service = Service(executable_path=chrome_driver_path)

    # Create ChromeOptions if needed
    chrome_options = webdriver.ChromeOptions()

    # Create the WebDriver instance using Service and ChromeOptions
    driver = webdriver.Chrome(service=service, options=chrome_options)


    yield driver
    driver.quit()
    # def fin():
    #     driver.quit()
    #
    # request.addfinalizer(fin)
    # return driver
