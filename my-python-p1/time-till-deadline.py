# import datetime
from datetime import datetime

user_input = input("enter your goal with a deadline separated by a colon, e.g.run errand:DD.MM.YYYY\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")   # y=23, Y=2023 refer documentation
today_date = datetime.today()
# calculating how many days from now to the deadline

time_till = deadline_date - today_date
# print(f"Dear user! time remaining for your goal: {goal} is {time_till.days} days")
hours_till = int(time_till.total_seconds() / 60 / 60)
print(f"Dear user! time remaining for your goal: {goal} is {hours_till} hours")
