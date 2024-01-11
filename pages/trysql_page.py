from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TrySqlPage:
    SQL_STATEMENT = (By.CSS_SELECTOR, ".CodeMirror-code")
    RUN_SQL_BUTTON = (By.XPATH, "//button[text()='Run SQL »']")
    NUMBER_OF_RECORDS_RETURNED = (By.XPATH, "//div[contains(text(), 'Number of Records:')]")
    TABLE_ROW = (By.CSS_SELECTOR, "table.w3-table-all tr:nth-child(1)")
    TEST_ELEM = (By.XPATH, "//h3[contains(text(), 'Result:')]")


    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all")
        try:
            self.driver.get("https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all")
        except TimeoutError:
            pass

    def click_run_sql(self):
        self.driver.find_element(*self.RUN_SQL_BUTTON).click()


    def check_returned_values(self):
        iframe_result_sql = self.driver.find_element(By.ID, "iframeResultSQL")
        self.driver.switch_to.frame(iframe_result_sql)

        number_of_records_element = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.NUMBER_OF_RECORDS_RETURNED))
        number_of_records_found = int(number_of_records_element.text.replace("Number of Records:", ''))
        print("I'm here")
        print(number_of_records_found)

        # element = self.driver.find_element(*self.NUMBER_OF_RECORDS_RETURNED)
        # text_of_element = element.text
        # print(text_of_element)




        self.driver.switch_to.default_content()





