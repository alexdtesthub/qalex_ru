import pytest

from pages.second_page_about import AboutMePage
from pages.locators import Links

link = Links.ABOUT_ME_LINK

@pytest.mark.about_page
def test_2nd_page_about_me(browser):
    about = AboutMePage(browser, link)
    about.open()
    about.should_be_all_links()
    about.go_to_main_link()
    about.go_to_make_offer_link()
    about.go_to_git_hub_link()
