import json
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self._cookie_login()
        else:
            self.driver = driver

    def _cookie_login(self):
        self.driver.get('https://work.weixin.qq.com')
        with open('cookies.json', 'r') as f:
            cookie = json.load(f)
        for i in cookie:
            self.driver.add_cookie(i)
        self.driver.maximize_window()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    def find_and_click(self, by, local):
        self.driver.find_element(by, local).click()

    def find_and_input(self, by, local, input_info):
        self.driver.find_element(by, local).send_keys(input_info)

    def manual_and_click(self, by, local):
        element = self.driver.find_element(by, local)
        ActionChains(self.driver).click(element).perform()

    def find_and_text(self, by, local):
        return self.driver.find_element(by, local).text
