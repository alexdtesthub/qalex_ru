from selenium.webdriver.common.by import By


class Links:
    MAIN_PAGE_LINK = 'https://qalex.ru/main_page/'
    ABOUT_ME_LINK = 'https://qalex.ru/about_page/'
    OFFER_PAGE_LINK = 'https://qalex.ru/offer_page/'
    GIT_PAGE_LINK = 'https://github.com/alexdtesthub'


class MainPageLocators:
    ABOUT_ME_LINK = (By.CSS_SELECTOR, 'a.about-me')
    MAKE_OFFER_LINK = (By.CSS_SELECTOR, 'a.make-offer')
    GIT_HUB_LINK = (By.CSS_SELECTOR, 'a.github')
    ALEX_TEXT = (By.CSS_SELECTOR, '.alexander-dorogin1')
    ALEX_LOGO = (By.CSS_SELECTOR, '.logo-icon')


class AboutMePageLocators:
    MAIN_LINK = (By.CSS_SELECTOR, 'a.back')
    ABOUT_ME_TEXT = (By.CSS_SELECTOR, '.selenium-python')


class OfferPageLocators:
    OFFER_FORM = (By.CSS_SELECTOR,  '.back1')
    HELLO_TEXT = (By.CSS_SELECTOR, '.hello-please-fill')
    MAIL_TEXT = (By.CSS_SELECTOR, '.mail')
    EMAIL_FIELD = (By.XPATH, '//*[@id="email"]')
    YOUR_OFFER_TEXT = (By.CSS_SELECTOR, '.your-offer')
    OFFER_FIELD = (By.XPATH, '//*[@id="your-offer"]')
    SEND_BUTTON = (By.CSS_SELECTOR, '.send')
    ALERT_TEXT = (By.CSS_SELECTOR, '.noty_body')
    OK_BUTTON = (By.CSS_SELECTOR, '.noty_body')
