from GymBookingBot import GymBookingBot
from BookingReporter import BookingReporter
from pathlib import Path
from dotenv import load_dotenv
import os

env_file = Path.cwd() / 'Python/.env'
load_dotenv(env_file)
PASSWORD = os.getenv('GYM_PASSWORD')
ACCOUNT = os.getenv('GYM_ACCOUNT')
GYM_URL = "https://appbrewery.github.io/gym/"

def main():

    class_names = {
        "yoga": "Yoga",
        "spin": "Spin",
        "hiit": "HIIT"
    }

    # Create the objects
    gym = GymBookingBot(
        account=ACCOUNT,
        password=PASSWORD,
        gym_url=GYM_URL,
        class_names=class_names
    )
    #It is not necessary to create an obj for Booking since we do not acces any attribute
    #we are just printing the functions values
    #reporter = BookingReporter()

    # Open website
    gym.start()

    # Login
    gym.log_in()

    # Calculate target dates
    target_dates = gym.get_target_dates()

    # Book classes
    print('Checking the classes...')

    processed_classes, total_target_classes = gym.check_classes(
        target_dates
    )

    # Print summary
    expected_bookings = BookingReporter.summary(
        processed_classes,
        total_target_classes
    )

    # Verify bookings
    gym.open_my_bookings()

    number_booking = gym.count_bookings()

    BookingReporter.verify(
        number_booking,
        expected_bookings
    )

main()