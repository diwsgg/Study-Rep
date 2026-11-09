import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException


class GymBookingBot:
    def __init__(self, account, password, gym_url, class_names):
        # User information
        self.account = account
        self.password = password

        # Website information
        self.gym_url = gym_url
        self.class_names = class_names

        # Selenium objects
        self.driver = None
        self.wait = None

    def start(self):

        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option(
            "detach", True
        )

        user_data_dir = os.path.join(
            os.getcwd(), "chrome_profile"
        )

        chrome_options.add_argument(
            f"--user-data-dir={user_data_dir}"
        )

        self.driver = webdriver.Chrome(
            options=chrome_options
        )

        self.driver.get(self.gym_url)

        self.wait = WebDriverWait(
            self.driver,
            15,
            poll_frequency=0.2,
            ignored_exceptions=(StaleElementReferenceException,)
        )