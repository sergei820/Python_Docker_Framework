from pages.trysql_page import TrySqlPage


def test_address_for_contactname(driver):
    """4. Обновить все поля (кроме CustomerID) в любой записи таблицы Customers и проверить, что изменения записались в базу."""