from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.utils import Utils


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

    def click_run_sql(self):
        self.driver.find_element(*self.RUN_SQL_BUTTON).click()

    def check_if_records_returned(self):
        iframe_result_sql = self.driver.find_element(By.ID, "iframeResultSQL")
        self.driver.switch_to.frame(iframe_result_sql)  # self.driver.switch_to.default_content()

        number_of_records_element = WebDriverWait(self.driver, 3).until(
            ec.visibility_of_element_located(self.NUMBER_OF_RECORDS_RETURNED))
        number_of_records_found = int(number_of_records_element.text.replace("Number of Records:", ''))
        assert number_of_records_found > 0

    def check_address_for_contact_name(self, expected_address: str, contact_name: str):
        customer_id = Utils.get_customer_id_by_text(self.driver, contact_name)
        actual_address = Utils.get_field_value_by_customer_id(self.driver, 'Address', customer_id)
        print(f"expected_address : {expected_address}")
        print(f"actual_address : {actual_address}")
        assert expected_address in actual_address

    def edit_select_request(self, reuqest_specification: str):
        pass


