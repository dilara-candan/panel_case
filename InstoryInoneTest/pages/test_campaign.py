from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TestCampaign(BasePage):
    CAMPAIGN_LIST = (By.CSS_SELECTOR, '#page .vuetable-body tr')
    TEST_LINK_MENU = (By.CSS_SELECTOR, '.is-test-link.test-link')
    VARIANT_ITEM = (By.CSS_SELECTOR, 'p[href*="inshoppingcart"].option__0')
    TEST_LINK = (By.CSS_SELECTOR, 'p[href*="inshoppingcart"].option__0 .option__child.option__0-child a')
    GENERATE_BUTTON = (By.CSS_SELECTOR, '#dropDownList > li.option__0 > a')

    def __init__(self, driver, campaign_information):
        super().__init__(driver)
        self.campaign_item = None
        self.campaign_information = campaign_information

    def campaign_check(self):
        if self.check_campaign_status():
            self.generate_javascript()
            self.open_campaign_with_test_link()
            self.check_campaign_in_html()

    def check_campaign_status(self):
        is_created_campaign = False
        self.find_element(*(By.CSS_SELECTOR, '[data-information*="' + str(self.campaign_information['campaign_name_id']) + '"]'))

        elements = self.find_elements(*self.CAMPAIGN_LIST)

        for element in elements:
            if "Test" in element.find_element(*(By.CSS_SELECTOR, '.camp-status')).text \
                    and element.find_element(*(By.CSS_SELECTOR, '[data-information*="' + str(self.campaign_information['campaign_name_id']) + '"]')):
                is_created_campaign = True

                self.campaign_item = element
                break

        return is_created_campaign

    def generate_javascript(self):
        for i in range(3):
            self.click_button_on_javascript(*self.GENERATE_BUTTON)
            self.wait(12)

    def open_campaign_with_test_link(self):
        self.campaign_item.find_element(*self.TEST_LINK_MENU).click()
        self.hover_element(*self.VARIANT_ITEM)

        test_url = self.find_element(*self.TEST_LINK).get_attribute('href')

        self.open_test_link_with_incognito_window(test_url)

    def check_campaign_in_html(self):
        self.find_element(*(By.CSS_SELECTOR, ('.ins-preview-wrapper-' + str(self.campaign_information['variant_id']))))