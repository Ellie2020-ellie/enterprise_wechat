import time

from page.main_page import MainPage


class TestAddEnterprise:

    def setup_class(self):
        # 实例化 MainPage类
        self.main = MainPage()

    def test_add_department(self):
        department_name = 'Ellie_10'
        party_name = self.main.goto_contact().click_add_department().enter_department_info(department_name)
        assert party_name == department_name
