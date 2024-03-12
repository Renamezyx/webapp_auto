from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DownloadPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://www.tiktok.com/studio/download"
        self.el_btn_download = (By.XPATH, '//*[@id="tiktok-live-main-container-id"]/div[2]/div/div[2]/button[1]')
        self.el_btn_login = (By.XPATH, '//*[@id="tiktok-live-main-container-id"]/div[2]/div/div[2]/button[2]')
        self.el_btn_free_download = (
            By.XPATH, '//*[@id="tiktok-live-main-container-id"]/section/div[1]/div[1]/section/div[2]/div/button[1]')
        self.el_btn_free_download = (
            By.XPATH, '//*[@id="tiktok-live-main-container-id"]/section/div[1]/div[3]/section[2]/div/div/button')
        self.el_btn_get_access = (
            By.XPATH, '//*[@id="tiktok-live-main-container-id"]/section/div[1]/div[1]/section/div[2]/div/button[2]')
        self.el_btn_see_more = (
            By.XPATH, '//*[@id="tiktok-live-main-container-id"]/section/div[1]/div[3]/section[1]/div[2]/a')

    def login(self, phone, vcode):
        self.click_element(self.el_btn_login)
        el_btn_login_type_phone = (By.XPATH, '//*[@id="loginContainer"]/div/div/div/div[2]/div[2]')
        el_inp_phone_number = (By.XPATH, '//*[@id="loginContainer"]/div[2]/form/div[2]/div/div[2]/input')
        el_inp_vcode = (By.XPATH, '//*[@id="loginContainer"]/div[2]/form/div[3]/div/div/input')
        el_btn_login_button = (By.XPATH, '//*[@id="loginContainer"]/div[2]/form/button')
        el_sel_country = (By.XPATH, '//*[@id="loginContainer"]/div[2]/form/div[2]/div/div[1]')
        el_inp_country = (By.XPATH, '//*[@id="login-phone-search"]')
        el_li_country = (By.XPATH, '//*[@id="CN-86"]')
        self.click_element(el_btn_login_type_phone)
        self.click_element(el_sel_country)
        self.enter_text(el_inp_country, "86")
        self.click_element(el_li_country)
        self.enter_text(el_inp_phone_number, phone)
        self.enter_text(el_inp_vcode, vcode)
        self.click_element(el_btn_login_button)

    def displayed_get_access(self):
        # 判断get access 按钮是否可见
        return self.find_element(self.el_btn_get_access).is_displayed()

    def open_page(self):
        self.open(self.base_url)
