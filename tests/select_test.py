from selenium import webdriver
from pages.trysql_page import TrySqlPage


def test_address_for_contactname():
    """Вывести все строки таблицы Customers и убедиться,
    что запись с ContactName равной 'Giovanni Rovelli'
    имеет Address = 'Via Ludovico il Moro 22'."""

    chrome_driver_path = "../driver/chromedriver_win.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    trySqlPage = TrySqlPage(driver)
    trySqlPage.open_page()
    trySqlPage.click_run_sql()

