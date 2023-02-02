from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    CREATE_CAMPAIGN_BUTTON = (By.ID, 'create-mobile-campaign')
    CAMPAIGN_NAME = (By.ID, 'campaign-name')
    CAMPAIGN_ACCEPT = (By.ID, 'accept')
    SAVE_AND_CONTINUE = (By.ID, 'save-and-next')
    ADD_NEW_VARIANT = (By.ID, 'add-new-variation')
    TEMPLATE = (By.CSS_SELECTOR, '.btn-select[template-id="89"]')
    NOTIFICATION_POPUP = (By.CSS_SELECTOR, '#inline-select-notification .inline-select-notification-confirm')
    AFTER_POSITION = (By.CSS_SELECTOR, '#select-element-menu li.append-after')
    SAVE_BUTTON = (By.CSS_SELECTOR, '#save[class="in-button-wrapper qa-button w-1 in-button-wrapper_fourth-secondary bor-r-0 bor-n h-1 w-13-s f-w-700 t-a-c t-t-u t-c-4"]')

    PAGE_RULES = (By.CSS_SELECTOR, '.page-rules.qa-page-rules')
    RULE_DROPDOWN = (By.ID, 'conditionList0')
    PAGE_TYPES = (By.CSS_SELECTOR, '.option__2.conditionList0-page-type')

    LANGUAGE_DROPDOWN = (By.ID, 'personalization-language')
    ALL_LANGUAGE = (By.CSS_SELECTOR, '.option__0.personalization-language-all-languages.option_active')
    NEVER_ENDS = (By.CSS_SELECTOR, '[for="Never Ends"]')
    CAMPAIGN_TEST_STATUS = (By.CSS_SELECTOR, '[for="Test"]')
    ADVANCED_SETTINGS = (By.XPATH, '//*[@id="page"]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[4]/a')
    PRIORITY_DROPDOWN = (By.XPATH, '//*[@id="priority"]')
    PRIORITY_OPTION = (By.CSS_SELECTOR, 'a.priority-1')
    NOTE = (By.ID, 'note')

    IFRAME_ID = 'ins-skeleton-partner-iframe'
    CAMPAIGN_LOCATION = 'site-branding'

    def __init__(self, driver):
        super().__init__(driver)

        self.campaign_name_id = self.get_current_timestamp()

    def create_campaign(self):
        # Click create campaign
        self.click_element(*self.CREATE_CAMPAIGN_BUTTON)

        # Set campaign name
        self.send_text("SEL - " + str(self.campaign_name_id), *self.CAMPAIGN_NAME)

        # Create campaign
        self.click_element(*self.CAMPAIGN_ACCEPT)

        # Skip segments page
        self.click_element(*self.SAVE_AND_CONTINUE)

        # Wait page switch
        self.wait(3)

        # Select Page Type All Page And Skip rules page
        self.wait_and_click_element(self.PAGE_RULES)
        self.wait_and_click_element(self.RULE_DROPDOWN)
        self.wait_and_click_element(self.PAGE_TYPES)

        self.wait_and_click_element(self.SAVE_AND_CONTINUE)

        # Add new variant
        self.click_element(*self.ADD_NEW_VARIANT)

        # Get campaign information
        url = self.get_url_paths()

        # Select campaign template
        self.click_element(*self.TEMPLATE)

        # Skip notification popup
        self.click_element(*self.NOTIFICATION_POPUP)

        # Select campaign position
        self.hover_and_click_element_in_iframe(self.IFRAME_ID, self.CAMPAIGN_LOCATION)
        self.click_element(*self.AFTER_POSITION)

        # Save campaign
        self.wait_and_click_element(self.SAVE_BUTTON)

        # Skip Variants page
        self.click_element(*self.SAVE_AND_CONTINUE)

        # Wait page switch
        self.wait(2)

        # Skip Goals page
        self.wait_and_click_element(self.SAVE_AND_CONTINUE)

        # Change campaign options
        self.click_button_on_javascript(*self.LANGUAGE_DROPDOWN)
        self.click_button_on_javascript(*self.ALL_LANGUAGE)
        self.click_button_on_javascript(*self.NEVER_ENDS)
        self.click_button_on_javascript(*self.ADVANCED_SETTINGS)
        self.click_button_on_javascript(*self.PRIORITY_DROPDOWN)
        self.click_button_on_javascript(*self.PRIORITY_OPTION)
        self.click_button_on_javascript(*self.CAMPAIGN_TEST_STATUS)
        self.send_text("CREATED CAMPAIGN", *self.NOTE)

        # Launch campaign
        self.wait_and_click_element(self.SAVE_AND_CONTINUE)

        return {
            'campaign_id': url[4],
            'variant_id': url[6],
            'campaign_name_id': self.campaign_name_id
        }
