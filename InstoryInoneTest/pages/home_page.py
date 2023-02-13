from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    EXPERIENCE_GROUP_SELECTOR = '.in-sidebar-wrapper__groups:nth-child(3)'
    OPTIMIZE_SELECTOR = EXPERIENCE_GROUP_SELECTOR + ' .in-sidebar-wrapper__opened ul li:nth-child(1)'
    INSTORY_SELECTOR = OPTIMIZE_SELECTOR + ' ul li:nth-child(2)'

    EXPERIENCE_GROUP = (By.CSS_SELECTOR, EXPERIENCE_GROUP_SELECTOR)
    OPTIMIZE = (By.CSS_SELECTOR, OPTIMIZE_SELECTOR)
    INSTORY = (By.CSS_SELECTOR, OPTIMIZE_SELECTOR)

    def select_web_instory_product(self):
        self.hover_and_click_element(*self.EXPERIENCE_GROUP)
        self.click_element(*self.OPTIMIZE)
        self.click_element(*self.INSTORY)
