from test.base_test import BaseTest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.test_campaign import TestCampaign


class InoneInstoryTest(BaseTest):
    def test_inone_instory_test(self):
        # Log in Inone Panel
        login_page = LoginPage(self.driver)

        login_page.fill_user_information_and_proceed("{username}", "{password}")

        # Select Web Instory on home page
        home_page = HomePage(self.driver)

        home_page.select_web_instory_product()

        # Create a new campaign on Product Page
        product_page = ProductPage(self.driver)

        campaign_information = product_page.create_campaign()

        # Test campaign
        test_campaign = TestCampaign(self.driver, campaign_information)

        test_campaign.campaign_check()

    def tear_down(self):
        self.driver.quit()
