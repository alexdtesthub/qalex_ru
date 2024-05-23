from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import MainPageLocators, AboutMePageLocators, OfferPageLocators, Links


class OfferPage(BasePage):
    def should_be_all_links(self):
        self.should_be_main_link()
        self.should_be_about_me_link()
        self.should_be_git_hub_link()


    def should_be_main_link(self):
        try:
            self.browser.find_element(*AboutMePageLocators.MAIN_LINK)
        except NoSuchElementException:
            assert False, "No MAIN_LINK found"

    def should_be_about_me_link(self):
        try:
            self.browser.find_element(*MainPageLocators.ABOUT_ME_LINK)
        except NoSuchElementException:
            assert False, "No ABOUT_ME_LINK found"

    def should_be_git_hub_link(self):
        try:
            self.browser.find_element(*MainPageLocators.GIT_HUB_LINK)
        except NoSuchElementException:
            assert False, "No GIT_HUB_LINK found"


    def should_be_all_elements_in_form(self):
        self.should_be_form()
        self.should_be_hello_text_in_form()
        self.should_be_mail_text_in_form()
        self.should_be_your_offer_text_in_form()
        self.should_be_send_button_in_form()


    def should_be_form(self):
        try:
            self.browser.find_element(*OfferPageLocators.OFFER_FORM)
        except NoSuchElementException:
            assert False, "No OFFER_FORM found"

    def should_be_hello_text_in_form(self):
        try:
            self.browser.find_element(*OfferPageLocators.HELLO_TEXT)
        except NoSuchElementException:
            assert False, "No HELLO_TEXT in form"

    def should_be_mail_text_in_form(self):
        try:
            self.browser.find_element(*OfferPageLocators.MAIL_TEXT)
        except NoSuchElementException:
            assert False, "No MAIL_TEXT in form"

    def should_be_your_offer_text_in_form(self):
        try:
            self.browser.find_element(*OfferPageLocators.YOUR_OFFER_TEXT)
        except NoSuchElementException:
            assert False, "No YOUR_OFFER_TEXT in form"

    def should_be_send_button_in_form(self):
        try:
            self.browser.find_element(*OfferPageLocators.SEND_BUTTON)
        except NoSuchElementException:
            assert False, "No SEND_BUTTON in form"

    def check_mail_and_offer_forms_and_send(self, email, offer):
        email_field = self.browser.find_element(*OfferPageLocators.EMAIL_FIELD)
        email_field.click()
        email_field.send_keys(email)
        offer_field = self.browser.find_element(*OfferPageLocators.OFFER_FIELD)
        offer_field.click()
        offer_field.send_keys(offer)
        send_button = self.browser.find_element(*OfferPageLocators.SEND_BUTTON)
        send_button.click()
        try:
            alert_text = self.browser.find_element(*OfferPageLocators.ALERT_TEXT).text
        except NoSuchElementException:
            assert False, "Alert text element not found"

        if alert_text == 'Your offer was sent':
            assert True, "No <Your offer was sent> in alert_text"
            ok_button = self.browser.find_element(*OfferPageLocators.OK_BUTTON)
            ok_button.click()

        elif alert_text == 'Email and your offer fields are required':
            assert True, "No <Email and your offer fields are required> in alert_text"
            ok_button = self.browser.find_element(*OfferPageLocators.OK_BUTTON)
            ok_button.click()

        elif alert_text == "This email has already been used. Wait for a reply by mail first":
            assert True, "No <This email has already been used. Wait for a reply by mail first> in alert_text"
            ok_button = self.browser.find_element(*OfferPageLocators.OK_BUTTON)
            ok_button.click()

        else:
            assert False, f"Unexpected alert_text: {alert_text}"

    def go_to_main_link(self):
        link = self.browser.find_element(*AboutMePageLocators.MAIN_LINK)
        link.click()
        new_page_url = Links.MAIN_PAGE_LINK
        assert new_page_url == self.browser.current_url, 'Incorrect Page URL on click Main'
        self.browser.back()

    def go_to_about_me_link(self):
        link = self.browser.find_element(*MainPageLocators.ABOUT_ME_LINK)
        link.click()
        new_page_url = Links.ABOUT_ME_LINK
        assert new_page_url == self.browser.current_url, 'Incorrect Page URL on click About Me'
        self.browser.back()

    def go_to_git_hub_link(self):

        initial_window_count = len(self.browser.window_handles)

        link = self.browser.find_element(*MainPageLocators.GIT_HUB_LINK)
        link.click()

        new_window_count = len(self.browser.window_handles)

        assert new_window_count == initial_window_count + 1, "No new handle at Git Hub button"

        self.browser.switch_to.window(self.browser.window_handles[-1])

        new_page_url = Links.GIT_PAGE_LINK
        assert new_page_url == self.browser.current_url, 'Incorrect Page URL on click Git Hub'
