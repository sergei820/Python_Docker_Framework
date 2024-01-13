from selenium.webdriver.common.by import By
import yaml
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Utils:
    @staticmethod
    def get_customer_id_by_text(driver, text_to_find) -> int:
        customer_id_selector = f"//td[contains(text(), '{text_to_find}')]/parent::tr/td[1]"
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

    @staticmethod
    def get_config_value(section, key):
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        return config[section][key]
