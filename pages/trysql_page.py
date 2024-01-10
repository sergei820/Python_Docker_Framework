from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TrySqlPage:
    SQL_STATEMENT = (By.CSS_SELECTOR, ".CodeMirror-code")
    RUN_SQL_BUTTON = (By.XPATH, "//button[text()='Run SQL »']")
    NUMBER_OF_RECORDS_RETURNED = (By.XPATH, "//div[contains(text(), 'Number of Records:')]")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all")
        try:
            self.driver.get("https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all")
        except TimeoutError:
            pass

        # url = "https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all"
        # self.driver.execute_script(f"window.location.href = '{url}';")
        # self.driver.execute_script("window.stop();")

        # editor_element = self.driver.find_element(By.ID,
        #                                      "textareaCodeSQL")
        # text_to_insert = "SELECT * FROM Customers;"
        # self.driver.execute_script(f"arguments[0].innerText = '{text_to_insert}';", editor_element)
        # self.driver.switch_to.default_content()

    def click_run_sql(self):
        self.driver.find_element(*self.RUN_SQL_BUTTON).click()
        # wait = WebDriverWait(self.driver, 3)
        # element = wait.until(EC.element_to_be_clickable(*self.RUN_SQL_BUTTON))
        #
        # element.click()
        # WebDriverWait(self.driver, 3).until(
        #     EC.visibility_of_element_located(*self.NUMBER_OF_RECORDS_RETURNED))
        time.sleep(5)

    # def check_if_request_executed(self):





