from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    EXPERIENCE_GROUP = (By.XPATH, '//*[@id="page"]/div/div[2]/div[1]/div/div/ul/li[3]')
    OPTIMIZE = (By.XPATH, '//*[@id="page"]/div/div[2]/div[1]/div/div/ul/li[3]/div/ul/li[1]')
    INSTORY = (By.XPATH, '//*[@id="page"]/div/div[2]/div[1]/div/div/ul/li[3]/div/ul/li[1]/ul/li[2]')

    def select_web_instory_product(self):
        self.hover_and_click_element(*self.EXPERIENCE_GROUP)
        self.click_element(*self.OPTIMIZE)
        self.click_element(*self.INSTORY)
