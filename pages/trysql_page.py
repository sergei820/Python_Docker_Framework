from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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

    def check_returned_values(self):
        iframe_result_sql = self.driver.find_element(By.ID, "iframeResultSQL")
        self.driver.switch_to.frame(iframe_result_sql)

        number_of_records_element = WebDriverWait(self.driver, 3).until(
            ec.visibility_of_element_located(self.NUMBER_OF_RECORDS_RETURNED))
        number_of_records_found = int(number_of_records_element.text.replace("Number of Records:", ''))
        print(number_of_records_found)

    def check_address_for_contact_name(self, expected_address: str, contact_name: str):
        customer_id = TrySqlPage.get_customer_id_by_text(self.driver, contact_name)
        actual_address = TrySqlPage.get_field_value_by_customer_id(self.driver, 'Address', customer_id)
        print(f"expected_address : {expected_address}")
        print(f"actual_address : {actual_address}")
        assert expected_address in actual_address

    @staticmethod
    def get_customer_id_by_text(driver, text_to_find) -> int:
        customer_id_selector = f"//td[contains(text(), '{text_to_find}')]/parent::tr/td[1]"
        print(f"SELECTOR: {customer_id_selector}")
        customer_id_element = driver.find_element(By.XPATH, customer_id_selector)
        customer_id = int(customer_id_element.text)
        return customer_id

    @staticmethod
    def get_field_value_by_customer_id(driver, field_name: str, customer_id: int) -> str:
        if field_name == 'CustomerName':
            column_index = 2
        elif field_name == 'ContactName':
            column_index = 3
        elif field_name == 'Address':
            column_index = 4
        elif field_name == 'City':
            column_index = 5
        elif field_name == 'PostalCode':
            column_index = 6
        elif field_name == 'Country':
            column_index = 7
        else:
            raise TypeError("Please, choose the correct column name")
        searched_element = driver.find_element(By.XPATH, f"//table[@class='w3-table-all notranslate']"
                                                              f"//tr[{str(customer_id + 1)}]/td[{column_index}]")
        field_value = searched_element.text
        return field_value

    # self.driver.switch_to.default_content()
