import pytest

from pages.trysql_page import TrySqlPage


@pytest.mark.skip
def test_insert_record(driver):
    """3. Добавить новую запись в таблицу Customers и проверить, что эта запись добавилась."""
    try_sql_page = TrySqlPage(driver)

    try_sql_page.open_page()
    try_sql_page.replace_request('INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) VALUES ("New Customer", "New Contact", "Some Addr", "SomeCity", "0043", "UK");')
    try_sql_page.click_run_sql()
    try_sql_page.switch_to_iframe_result_sql()
    try_sql_page.check_address_for_contact_name('Some Addr', 'New Contact')
    # Test fails, w3school returns error on INSERT operation:
    # Your browser does not support WebSQL, so you are now using a light-version of our Try-SQL Editor,
    # with a read-only Database.
    # If you use a browser with WebSQL support (Chrome, Safari, or Opera),   -> I'm using Chrome
    # you can try any SQL statement, and play with the Database as much as you like.
