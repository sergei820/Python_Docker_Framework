import pytest
from pages.trysql_page import TrySqlPage


#@pytest.mark.skip
def test_update_operation(driver_fixture):
    """4. Обновить все поля (кроме CustomerID) в любой записи таблицы Customers
    и проверить, что изменения записались в базу."""
    try_sql_page = TrySqlPage(driver_fixture)

    try_sql_page.open_page()
    try_sql_page.replace_request(
        'UPDATE Customers SET CustomerName = "NewName", ContactName = "NewContactName", Address = "NewAddr", '
        'City = "NewCity", PostalCode = "NewPostalCode", Country = "NewCountry" WHERE CustomerID = 4;')
    try_sql_page.click_run_sql()
    try_sql_page.replace_request('SELECT * FROM Customers;')
    try_sql_page.click_run_sql()
    # try_sql_page.switch_to_iframe_result_sql()  # not needed in Chrome 114 (used in Docker)
    try_sql_page.check_address_for_contact_name('NewAddr', 'NewContactName')
