
from pages.trysql_page import TrySqlPage


def test_address_for_contactname(driver):
    """Вывести все строки таблицы Customers и убедиться,
    что запись с ContactName равной 'Giovanni Rovelli'
    имеет Address = 'Via Ludovico il Moro 22'."""

    try_sql_page = TrySqlPage(driver)
    try_sql_page.open_page()
    try_sql_page.click_run_sql()
    try_sql_page.check_returned_values()
    try_sql_page.check_address_for_contactname('Via Ludovico il Moro 22', 'Giovanni Rovelli')

