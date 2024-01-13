import pytest
from pages.trysql_page import TrySqlPage


@pytest.mark.skip
def test_delete(chrome_driver):
    """5. Придумать собственный автотест и реализовать (тут все ограничивается только вашей фантазией)"""
    try_sql_page = TrySqlPage(chrome_driver)

    try_sql_page.open_page()
    try_sql_page.replace_request('DELETE FROM Customers WHERE CustomerID = 5')
    try_sql_page.click_run_sql()

    try_sql_page.replace_request('SELECT * FROM Customers;')
    try_sql_page.click_run_sql()
    try_sql_page.switch_to_iframe_result_sql()
    try_sql_page.check_returned_records_number(90)
