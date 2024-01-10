
from pages.trysql_page import TrySqlPage


def test_address_for_contactname(driver):
    """Вывести все строки таблицы Customers и убедиться,
    что запись с ContactName равной 'Giovanni Rovelli'
    имеет Address = 'Via Ludovico il Moro 22'."""



    trySqlPage = TrySqlPage(driver)
    trySqlPage.open_page()
    trySqlPage.click_run_sql()

