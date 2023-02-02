from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    LOG_IN_BUTTON = (By.ID, 'login-button')

    def fill_user_information_and_proceed(self, email, password):
        self.send_text(email, *self.EMAIL)
        self.send_text(password, *self.PASSWORD)

        self.click_element(*self.LOG_IN_BUTTON)
