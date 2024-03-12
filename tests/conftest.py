import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # 可以在这里进行一些共享的配置，例如窗口大小、隐式等待时间等
    driver.maximize_window()
    driver.implicitly_wait(10)

    # 返回 WebDriver 对象，以便在测试用例中使用
    yield driver

    # 在测试用例执行完成后关闭浏览器
    driver.quit()
