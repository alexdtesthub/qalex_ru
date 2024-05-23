import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()  # или webdriver.Firefox(), webdriver.Edge() и т.д.
    yield driver
    driver.quit()