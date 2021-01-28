import time

from page.add_department_page import AddDepartmentPage
from page.base_page import BasePage


class ContactPage(BasePage):
    def click_add_department(self):
        time.sleep(2)
        # 点击添加
        self.find_and_click('xpath', "//i[@class='member_colLeft_top_addBtn']")
        # 点击添加部门
        self.find_and_click('xpath', "//a[@class='js_create_party']")
        return AddDepartmentPage(self.driver)


