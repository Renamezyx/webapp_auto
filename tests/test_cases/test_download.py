import pytest
import requests

from data.account import get_account
from pages.download_page import DownloadPage
from utils.logger_base import logger


@pytest.fixture(scope="class")
def download_page(driver):
    return DownloadPage(driver)


class TestDownloadPage:

    def test_check_links(self, download_page):
        download_page.open_page()
        links = download_page.get_links()
        flags = []
        for link in links:
            res = requests.get(link.get_attribute("href"), allow_redirects=False)
            logger.info(f"{link.get_attribute("href")} :{res.status_code}")
            if res.status_code == 200:
                flags.append(True)
            elif res.status_code == 302 and res.headers['Location'].find("404") == -1:
                logger.warn(f"重定向: {res.headers['Location']}")
                flags.append(True)
            else:
                flags.append(False)
        assert all(flags)

    ############################################以上是登录前的case############################################

    @pytest.mark.parametrize("account", [get_account()])
    def test_login(self, download_page, account):
        download_page.open_page()
        download_page.login(phone=account["phone"], vcode=account["code"], country=account["country"])
        assert download_page.profile_visible()

############################################以下是登录后的case############################################
