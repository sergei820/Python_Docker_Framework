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
        print("I'm here")
        print(number_of_records_found)

        # element = self.driver.find_element(*self.NUMBER_OF_RECORDS_RETURNED)
        # text_of_element = element.text
        # print(text_of_element)
        self.driver.switch_to.default_content()

    def check_address_for_contact_name(self, address: str, contact_name: str):
        """ContactName               'Giovanni Rovelli'        имеет
        Address = 'Via Ludovico il Moro 22'.        """

    def get_customer_id_by_text(self, text_to_find):
        customer_id_element = self.driver.find_element(By.XPATH, f"//td[contains(text(), '{text_to_find}')]/parent::tr/td[1]")
        return int(customer_id_element.text)
# //table[@class='w3-table-all notranslate']//tr/td[1]
