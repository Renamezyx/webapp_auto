import time

from pages.download_page import DownloadPage


def test_login(driver):
    download_page = DownloadPage(driver)
    download_page.open_page()
    download_page.login("12342058061", "001862")
    time.sleep(10)
    assert download_page.displayed_get_access()
