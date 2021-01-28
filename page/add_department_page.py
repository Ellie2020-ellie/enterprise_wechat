import time

from page.base_page import BasePage


# from page.contact_page import ContactPage


class AddDepartmentPage(BasePage):
    def enter_department_info(self, departement_name):
        self.find_and_input('xpath', "//input[@class='qui_inputText ww_inputText' and @name='name']", departement_name)
        self.find_and_click('xpath', "//span[@class='js_parent_party_name']")
        time.sleep(1)
        self.manual_and_click('xpath', "//form//a[@id='1688850205947304_anchor']")
        self.find_and_click('xpath', "//a[@d_ck='submit']")
        time.sleep(10)
        party_name = self.find_and_text('xpath', "//*[@id='party_name']")
        return party_name
