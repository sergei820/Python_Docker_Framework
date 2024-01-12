from pages.trysql_page import TrySqlPage


def test_update_operation(driver):
    """4. Обновить все поля (кроме CustomerID) в любой записи таблицы Customers и проверить, что изменения записались в базу."""
    'UPDATE Customers SET "CustomerID" = 4, "CustomerName" = "NewName", "ContactName" = "NewContactName", "Address" = "NewAddr", "City" = "NewCity", "PostalCode" = "NewPostalCode", "Country" = "NewCountry" WHERE "CustomerID" = 4;'
    pass

