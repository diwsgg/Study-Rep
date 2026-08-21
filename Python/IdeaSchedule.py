
'''
The idea is to asked to the user, the time he will start an activity
and the amount of time he would like to spent on that activity

Like work, that are most of the time 8hrs, if he starts at 7am when he will stop, (including the hour to eat)
so 7 am + 8hrs work + 1hr to eat --> 4 pm

We can asked to the user, 
Start time, Hours to spent on the activity, Hours to eat,(And after consider the time of the activity, we can choose when is the best time to eat, iof needed)

This can be display with a temporizer if he would like  putting animations, or changing the time color, depending on the time of the day.

In mexico after 6fhrs of consecutive work, the workers have right to eat.
'''


print("Welcome to the Schedule Visualizier")

#String ? 1:30, its a string but we can divided by hour and minutes for a best manage

start_time_hours = int(input("What hour are you going to start the activity: (Just the number like 1, 12, 7)"))

while start_time_hours <=0 or start_time_hours>= 13:
    print("Invalid hours")
    start_time_hours = int(input("Type the start hours again"))


start_time_mins = int("Also the minutes that you going to start the activity: (Just the number like 20, 30, 45)")

while start_time_mins <0 or start_time_mins > 60:
    print("Invalid minutes")
    start_time_mins = int(input("Type the start minutes again"))

#So we have to decide also the time like if the user put 12 next hour is 1pm or could be 1am depending the shift

shift = int(input("What shift are you working on [1.'AM', 2.'PM']"))

