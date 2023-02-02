from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locators):
        return self.driver.find_element(*locators)

    def find_elements(self, *locators):
        return self.driver.find_elements(*locators)

    def click_element(self, *locators):
        self.find_element(*locators).click()

    def send_text(self, text, *locators):
        self.find_element(*locators).send_keys(text)

    def hover_and_click_element(self, *locators):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(*locators)).click().perform()

    def hover_element(self, *locators):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(*locators)).perform()

    def wait_and_click_element(self, locators):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(locators)).click()

    def hover_and_click_element_in_iframe(self, iframeID, element):
        IFRAME_ID = (By.ID, iframeID)
        ELEMENT = (By.ID, element)

        self.driver.switch_to.frame(self.find_element(*IFRAME_ID))

        self.hover_and_click_element(*ELEMENT)

        self.driver.switch_to.default_content()

    def wait(self, second):
        time.sleep(second)

    def get_current_timestamp(self):
        return round(time.time() * 1000)

    def click_button_on_javascript(self, *locators):
        self.driver.execute_script("arguments[0].click();", self.find_element(*locators))

    def get_url_paths(self):
        url = self.driver.current_url

        return url.split("/")

    def open_test_link_with_incognito_window(self, url):
        options = Options()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')
        options.add_argument("--incognito")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.implicitly_wait(10)