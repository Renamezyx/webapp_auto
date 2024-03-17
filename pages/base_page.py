import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # 可以在这里进行一些共享的配置，例如窗口大小、隐式等待时间等
        driver.maximize_window()
        driver.implicitly_wait(10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def wait_for_element_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def is_element_visible(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    def take_screenshot(self, filename):
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        filepath = os.path.join(screenshots_dir, filename)
        self.driver.save_screenshot(filepath)

    def __del__(self):
        self.driver.quit()
