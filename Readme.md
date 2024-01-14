Task:

Используя любой язык программирования необходимо написать следующие автотесты для сайта https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all
1. Вывести все строки таблицы Customers и убедиться, что запись с ContactName равной 'Giovanni Rovelli' имеет Address = 'Via Ludovico il Moro 22'.
2. Вывести только те строки таблицы Customers, где city='London'. Проверить, что в таблице ровно 6 записей.
3. Добавить новую запись в таблицу Customers и проверить, что эта запись добавилась.
4. Обновить все поля (кроме CustomerID) в любой записи таблицы Customers и проверить, что изменения записались в базу.
5. Придумать собственный автотест и реализовать (тут все ограничивается только вашей фантазией).
Заполнить поле ввода можно с помощью js кода, используя объект window.editor.
Требования:
- Для реализации обязательно использовать Selenium WebDriver
- Тесты должны запускаться в docker контейнере
- Код автотестов нужно выложить в любой git-репозиторий

To run the framework:
    
    docker-compose up -d
    pytest tests


Rewrite dockerfile, to run the framework automatically as part of docker-compose

what should be done:
python -m pip install --upgrade pip
pip install pytest
pip install selenium
pip install webdriver_manager
pip install pyyaml
pip install --upgrade webdriver_manager
pip install --upgrade selenium


On Mac:
pip3 install --upgrade pip
pip3 install pytest
pip3 install selenium
pip3 install webdriver_manager
pip3 install pyyaml


DELETE, UPDATE, INSERT operations work in Chrome Version 111.0.5563.64 (Official Build) (arm64)
but iframe doesn't work

https://stackoverflow.com/questions/77461398/w3schools-com-features-dont-work-in-latest-chrome-version
Google has removed the ability to use WebSQL in Chrome version 119: Intent to Deprecate and Remove Web SQL

So, the solution is: use Chrome 114 (check), that will allow DELETE, UPDATE, INSERT
and able to use WebSQL at  the same time

TODO:
dockerfile for running in one command
parametrize driver choosing
invent more interesting own test scenario