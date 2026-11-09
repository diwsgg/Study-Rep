import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

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

    def interact_element(self, name, action, message=''):
        locator = (By.ID, name)
        if action == 'click':
            self.wait.until(
                EC.element_to_be_clickable(locator)
            ).click()
        elif action == 'type':
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            element.send_keys(message)
        else:
            raise ValueError(f'Unknown action: {action}')

    def log_in(self):
        #login
        self.interact_element('login-button', 'click')
        #information
        self.interact_element('email-input', 'type', self.account)
        self.interact_element('password-input', 'type', self.password)
        #submit
        self.interact_element('submit-button', 'click')

    def get_schedule_date(self):
        title = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'Schedule_scheduleTitle__zfZxg')
            )
        )

        title_text = title.text

        date_text = (
            title_text.split('Today: ')[1]
            .replace(')', '')
            .strip()
        )

        return datetime.strptime(date_text,'%m/%d/%Y').date()

    def check_resting_days(self, amount, today):
        days_until = (amount - today.weekday()) % 7
        return days_until

    def convert_date(self, days_until, today):
        next_date = today + timedelta(days=days_until)
        return next_date.strftime('%Y-%m-%d')

    def get_target_dates(self):
        today = self.get_schedule_date()

        days_until_tuesday = self.check_resting_days(1, today)
        days_until_thursday = self.check_resting_days(3, today)

        next_tuesday = self.convert_date(days_until_tuesday, today)
        next_thursday = self.convert_date(days_until_thursday, today)
        #THE Diference is that we are returning a set
        return {
            next_tuesday + '-1800',
            next_thursday + '-1800'
        }