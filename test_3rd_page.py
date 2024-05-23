import pytest
from faker import Faker
from pages.third_page_offer import OfferPage
from pages.locators import Links
import mysql.connector

link = Links.OFFER_PAGE_LINK

# Фикстура для параметров подключения к базе данных
@pytest.fixture(scope="session")
def db_config():
    return {
        'host': 'localhost',
        'user': 'root',
        'password': '',  # Укажите свой пароль
        'database': 'my_database'
    }

# Фикстура для случайного email (сессионная)
@pytest.fixture(scope="session")
def random_email():
    fake = Faker()
    return fake.email()

@pytest.fixture(params=[
    (None, "Valid Offer"),  # Успешный случай
    (None, "Valid Offer"),  # Дублирование уже созданного запроса
    ("", "Valid Offer"),  # Отсутствующий email
    ("valid@email.com", ""),  # Отсутствующее offer
    ("", "")  # Оба поля пустые
], ids=["success", "duplicate", "no_email", "no_offer", "empty"])
def test_data(request, random_email):
    email, offer = request.param
    if email is None:
        email = random_email
    return email, offer

# Функция для проверки наличия/отсутствия данных в базе данных
def check_database(db_config, email, offer, expected_in_db):
    print(f"Вызов check_database с параметрами: {db_config}, {email}, {offer}, {expected_in_db}")
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE email = %s AND offer = %s"
    cursor.execute(query, (email, offer))
    result = cursor.fetchone()

    if expected_in_db:
        assert result is not None, f"Валидные данные не найдены в базе данных для email: {email}, offer: {offer}"
        assert cursor.rowcount == 1, f"Найдена дублирующая запись для email: {email}, offer: {offer}"
    else:
        assert result is None, f"Невалидные данные найдены в базе данных для email: {email}, offer: {offer}"

    cursor.close()
    connection.close()
    print("Выход из check_database")


@pytest.mark.offer_page
def test_3rd_page_offer(browser, test_data, db_config):
    email, offer = test_data
    yo_offer = OfferPage(browser, link)
    yo_offer.open()
    yo_offer.should_be_all_links()
    yo_offer.should_be_all_elements_in_form()
    yo_offer.check_mail_and_offer_forms_and_send(email, offer)
    yo_offer.go_to_main_link()
    yo_offer.go_to_about_me_link()
    yo_offer.go_to_git_hub_link()

    # Проверяем наличие/отсутствие данных в базе данных
    expected_in_db = email != "" and offer != ""
    check_database(db_config, email, offer, expected_in_db)