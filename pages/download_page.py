import requests
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DownloadPage(BasePage):
    def __init__(self, driver):
        xpath_by_text = {"english": {"Free_download_for_Windows": "Free download for Windows",
                                     "Get_access": "Get access"}}
        super().__init__(driver)
        self.base_url = "https://www.tiktok.com/studio/download?enter_from=profile&lang=en"
        self.el_btn_download = (By.XPATH, '//*[@data-e2e="top-login-button"][1]')
        self.el_btn_login = (By.XPATH, '//*[@data-e2e="top-login-button"][2]')
        self.el_btn_free_download = (
            By.XPATH,
            f'//*[@id="tiktok-live-main-container-id"]//button[text()="{xpath_by_text["english"]["Free_download_for_Windows"]}"]')
        self.el_btn_get_access = (
            By.XPATH,
            f'//*[@id="tiktok-live-main-container-id"]//button[text()="{xpath_by_text["english"]["Get_access"]}"]')
        self.el_links = (
            By.XPATH, '//*[@id="tiktok-live-main-container-id"]//a')

        self.el_profile = (By.XPATH, '//*[@data-e2e="profile-icon"]')

    def open_page(self):
        self.open(self.base_url)

    def login(self, phone, vcode, country):
        el_btn_login_type_phone = (By.XPATH, '//*[@id="loginContainer"]//div[text()="Use phone / email / username"]')
        el_inp_phone_number = (By.XPATH, '//*[@id="loginContainer"]//input[@name="mobile"]')
        el_inp_vcode = (By.XPATH, '//*[@id="loginContainer"]//div[contains(@class, "code-input")]/input')
        el_btn_login_button = (By.XPATH, '//*[@id="loginContainer"]//button[@type="submit"]')
        el_sel_country = (
            By.XPATH, '//*[@id="loginContainer"]//div[@aria-controls="phone-country-code-selector-wrapper"]')
        el_inp_country = (By.XPATH, '//*[@id="login-phone-search"]')
        el_li_country = (By.XPATH, f'//*[@id="{country}"]')
        if not self.is_element_visible(locator=el_inp_country, timeout=3):
            self.click_element(self.el_btn_login)
        self.click_element(el_btn_login_type_phone)
        self.click_element(el_sel_country)
        self.enter_text(el_inp_country, "86")
        self.click_element(el_li_country)
        self.enter_text(el_inp_phone_number, phone)
        self.enter_text(el_inp_vcode, vcode)
        self.click_element(el_btn_login_button)

    def get_links(self):
        links = self.find_elements(self.el_links)
        return links

    def profile_visible(self, timeout=3):
        return self.is_element_visible(locator=self.el_profile, timeout=timeout)
