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

    def find_all_buttons(self):
        return self.wait.until(
            EC.visibility_of_all_elements_located((
                By.CSS_SELECTOR,
                "button[id^='book-button-']"
            ))
        )

    def check_day(self, button_id, target_dates):
        date_tag = '-'.join(button_id.split('-')[3:])
        return date_tag in target_dates

    def get_date_title(self, button):
        day_group = button.find_element(
            By.XPATH,
            "ancestor::div[starts-with(@id, 'day-group-')][1]"
        )
        return day_group.find_element(
            By.CSS_SELECTOR, "h2"
        ).text.strip()

    def check_classes(self, target_dates):

        processed_classes = []
        total_target_classes = 0

        all_buttons = self.find_all_buttons()

        # Save IDs before interacting with the page
        button_ids = [
            button.get_attribute('id')
            for button in all_buttons
        ]

        for button_id in button_ids:

            is_target = self.check_day(
                button_id, target_dates
            )

            if is_target:
                total_target_classes += 1

            # Find the element again to avoid stale references
            button = self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, button_id)
                )
            )

            button_text = ' '.join(
                button.text.split()
            ).casefold()

            date_label = self.get_date_title(button)

            schedule_class = button_id.split('-')[2]

            class_name = self.class_names.get(
                schedule_class,
                schedule_class.title()
            )

            status = None

            if button_text == 'book class' and is_target:

                button.click()

                print(
                    f'Clicked Book Class for: '
                    f'{class_name} Class on {date_label}'
                )

                status = 'New Booking'

            elif button_text == 'join waitlist' and is_target:

                button.click()

                print(
                    f'Joined waitlist for: '
                    f'{class_name} Class on {date_label}'
                )

                status = 'New Waitlist'

            elif button_text == 'booked':

                print(
                    f'Already booked: '
                    f'{class_name} Class on {date_label}'
                )

                status = 'Already Booked'

            elif button_text == 'waitlisted':

                print(
                    f'Already on waitlist: '
                    f'{class_name} Class on {date_label}'
                )

                status = 'Already Waitlisted'

            if status is not None:

                processed_classes.append({
                    'class': class_name,
                    'date': date_label,
                    'status': status
                })

        return processed_classes, total_target_classes

    def open_my_bookings(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, 'My Bookings')
            )
        ).click()

    def count_bookings(self):

        booking_classes = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div[id^='booking-card-booking_']"
        )

        waitlist_classes = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div[id^='waitlist-card-waitlist_']"
        )

        print('\n--- VERIFYING ON MY BOOKINGS PAGE ---')
        #python will concatenate both [list1]+[list2] [1,2,3]+[8,5,7] = [1,2,3,8,5,7] like this
        #this works because both are lists, It doesn't work with every possible pair of iterables.
        for booking in booking_classes + waitlist_classes:

            class_name = booking.find_element(
                By.CSS_SELECTOR, 'h3'
            ).text.strip()

            print(f'✓ Verified: {class_name}')

        return len(booking_classes) + len(waitlist_classes)