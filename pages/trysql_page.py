from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TrySqlPage:
    SQL_STATEMENT = (By.CSS_SELECTOR, ".CodeMirror-code")
    RUN_SQL_BUTTON = (By.XPATH, "//button[text()='Run SQL »']")
    NUMBER_OF_RECORDS_RETURNED = (By.XPATH, "//div[contains(text(), 'Number of Records:')]")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        print("loading the page...")
        self.driver.get("https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all")
        # url = "https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all"
        # self.driver.execute_script(f"window.location.href = '{url}';")
        print("the page is loaded")

    def click_run_sql(self):
        self.driver.find_element(*self.RUN_SQL_BUTTON).click()
        # wait = WebDriverWait(self.driver, 3)
        # element = wait.until(EC.element_to_be_clickable(*self.RUN_SQL_BUTTON))
        #
        # element.click()
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(*self.NUMBER_OF_RECORDS_RETURNED))

    # def check_if_request_executed(self):





