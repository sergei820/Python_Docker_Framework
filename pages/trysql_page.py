from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.utils import Utils


class TrySqlPage:
    SQL_STATEMENT = (By.CSS_SELECTOR, ".CodeMirror-code")
    RUN_SQL_BUTTON = (By.XPATH, "//button[text()='Run SQL »']")
    NUMBER_OF_RECORDS_RETURNED = (By.XPATH, "//div[contains(text(), 'Number of Records:')]")
    ROWS_IN_RESULT_TABLE = (By.CSS_SELECTOR, "table.w3-table-all tr")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        # base_url = Utils.get_config_value('TestConfig', 'base_url')
        # trysql_page_uri = Utils.get_config_value('TestConfig', 'trysql_page_uri')
        # self.driver.get(base_url + trysql_page_uri)
        self.driver.get("https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all")  # hardcoded for docker

    def click_run_sql(self):
        run_sql_button = WebDriverWait(self.driver, 3).until(
            ec.element_to_be_clickable(self.RUN_SQL_BUTTON))
        run_sql_button.click()

    def switch_to_iframe_result_sql(self):
        iframe_result_sql = self.driver.find_element(By.ID, "iframeResultSQL")
        # WebDriverWait(self.driver, 10).until(ec.frame_to_be_available_and_switch_to_it(iframe_result_sql))
        self.driver.switch_to.frame(iframe_result_sql)  # self.driver.switch_to.default_content()

    def check_address_for_contact_name(self, expected_address: str, contact_name: str):
        customer_id = Utils.get_customer_id_by_text(self.driver, contact_name)
        actual_address = Utils.get_field_value_by_customer_id(self.driver, 'Address', customer_id)
        assert expected_address in actual_address

    def edit_select_request(self, reuqest_specification: str):
        js = f"""
        var cm = document.querySelector('.CodeMirror').CodeMirror;
        cm.setValue('SELECT * FROM Customers {reuqest_specification};');
        """
        self.driver.execute_script(js)

    def replace_request(self, sql_reuqest: str):
        js = f"""
                var cm = document.querySelector('.CodeMirror').CodeMirror;
                cm.setValue('{sql_reuqest}');
                """
        self.driver.execute_script(js)

    def check_returned_records_number(self, expected_records_number: int):
        number_of_records_element = WebDriverWait(self.driver, 3).until(
            ec.visibility_of_element_located(self.NUMBER_OF_RECORDS_RETURNED))
        number_of_records_found = int(number_of_records_element.text.replace("Number of Records:", ''))
        assert number_of_records_found == expected_records_number

        rows_in_table = self.driver.find_elements(*self.ROWS_IN_RESULT_TABLE)
        assert len(rows_in_table) == expected_records_number + 1  # table header is an additional row


