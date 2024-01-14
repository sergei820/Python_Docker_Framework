import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def remote_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = 'eager'  # 'normal' probably will work with chrome 114
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--log-level=3')

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=chrome_options
    )
    driver.implicitly_wait(1)
    yield driver
    driver.quit()


@pytest.fixture
def chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.page_load_strategy = 'eager'
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--log-level=3')

    chrome_driver_path = ChromeDriverManager().install()
    service = Service(executable_path=chrome_driver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(1)
    yield driver
    driver.quit()


@pytest.fixture
def ff_driver():
    ff_options = webdriver.FirefoxOptions()
    ff_options.page_load_strategy = 'eager'
    ff_options.add_argument('--allow-insecure-localhost')
    ff_options.add_argument('--ignore-certificate-errors')
    ff_options.add_argument("--ignore-ssl-errors")
    ff_options.add_argument('--disable-dev-shm-usage')

    firefox_driver_path = GeckoDriverManager().install()
    service = Service(executable_path=firefox_driver_path)
    driver = webdriver.Firefox(service=service, options=ff_options)

    driver.implicitly_wait(1)
    yield driver
    driver.quit()
