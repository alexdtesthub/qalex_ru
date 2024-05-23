import pytest

from pages.first_page_main import MainPage
from pages.locators import Links

link = Links.MAIN_PAGE_LINK

@pytest.mark.main_page
def test_1st_page_main(browser):
    main = MainPage(browser, link)
    main.open()
    main.should_be_all_links()
    main.go_to_about_me_link()
    main.go_to_make_offer_link()
    main.go_to_git_hub_link()
