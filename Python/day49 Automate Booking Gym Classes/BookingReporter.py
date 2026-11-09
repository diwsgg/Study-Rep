from datetime import datetime, timedelta

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Dates_check():

    def check_resting_days(amount,today):
        days_until = (amount - today.weekday()) % 7
        return days_until
    
    def convert_date(days_until, today):
        next_date = today + timedelta(days=days_until)
        #and we convert the date into a string
        date_string = next_date.strftime("%Y-%m-%d")
        return date_string
    
    def check_day(button, next_tuesday, next_thursday):
        #all at once
        date_tag = ('-').join((button.split('-')[3:]))
        #and then we compare
        #We can return the Boolean expression directly. There's no need for an additional if.
        return date_tag in (next_tuesday, next_thursday)
    
    def getToday(wait):
        title = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'Schedule_scheduleTitle__zfZxg'))
        )
        title = title.text
        #Example of output, Class Schedule (Today: 11/9/2026)
        #we just wanted the date
        title = title.split('Today: ')[1].replace(")", "")
        #convert to datetime
        schedule_date = datetime.strptime(title, "%m/%d/%Y").date()
        return schedule_date
    
    def tuesday_thursday(wait):
        #calculate for tuesday and thursday
        today = Dates_check.getToday(wait)

        days_until_tuesday = Dates_check.check_resting_days(1, today)
        days_until_thursday = Dates_check.check_resting_days(3, today)

        next_tuesday = Dates_check.convert_date(days_until_tuesday, today)
        next_thursday = Dates_check.convert_date(days_until_thursday, today)
        #add the hour (6 pm)
        next_tuesday+='-1800'
        next_thursday+='-1800'

        return next_tuesday, next_thursday