from selenium.common.exceptions import NoSuchElementException


from .base_page import BasePage
from .locators import MainPageLocators, Links



class MainPage(BasePage):
    def should_be_all_links(self):
        self.should_be_about_me_link()
        self.should_be_make_offer_link()
        self.should_be_git_hub_link()
        self.should_be_alex_text()
        self.should_be_alex_logo()


    def should_be_about_me_link(self):
        try:
            self.browser.find_element(*MainPageLocators.ABOUT_ME_LINK)
        except NoSuchElementException:
            assert False, "No ABOUT_ME_LINK found"

    def should_be_make_offer_link(self):
        try:
            self.browser.find_element(*MainPageLocators.MAKE_OFFER_LINK)
        except NoSuchElementException:
            assert False, "No MAKE_OFFER_LINK found"

    def should_be_git_hub_link(self):
        try:
            self.browser.find_element(*MainPageLocators.GIT_HUB_LINK)
        except NoSuchElementException:
            assert False, "No GIT_HUB_LINK found"



    def should_be_alex_text(self):
        try:
            self.browser.find_element(*MainPageLocators.ALEX_TEXT)
        except NoSuchElementException:
            assert False, "No ALEX_TEXT found"

    def should_be_alex_logo(self):
        try:
            self.browser.find_element(*MainPageLocators.ALEX_LOGO)
        except NoSuchElementException:
            assert False, "No ALEX_LOGO found"


    def go_to_about_me_link(self):
        link = self.browser.find_element(*MainPageLocators.ABOUT_ME_LINK)
        link.click()
        new_page_url = Links.ABOUT_ME_LINK
        assert new_page_url == self.browser.current_url, 'Incorrect Page URL on click About Me'
        self.browser.back()

    def go_to_make_offer_link(self):
        link = self.browser.find_element(*MainPageLocators.MAKE_OFFER_LINK)
        link.click()
        new_page_url = Links.OFFER_PAGE_LINK
        assert new_page_url == self.browser.current_url, 'Incorrect Page URL on click Make Offer'
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
