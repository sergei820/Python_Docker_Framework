
from pages.trysql_page import TrySqlPage


def test_address_for_contactname(driver):
    """Вывести все строки таблицы Customers и убедиться,
    что запись с ContactName равной 'Giovanni Rovelli'
    имеет Address = 'Via Ludovico il Moro 22'."""
    try_sql_page = TrySqlPage(driver)

    try_sql_page.open_page()
    try_sql_page.click_run_sql()
    try_sql_page.check_if_records_returned()
    try_sql_page.check_address_for_contact_name('Via Ludovico il Moro 22', 'Giovanni Rovelli')


def test_records_number_for_specific_city(driver):
    """2. Вывести только те строки таблицы Customers, где city='London'. Проверить, что в таблице ровно 6 записей."""
    try_sql_page = TrySqlPage(driver)
    try_sql_page.open_page()
    try_sql_page.edit_select_request("WHERE city='London'")

