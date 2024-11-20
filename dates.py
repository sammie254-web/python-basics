#dates
from datetime import date, timedelta, datetime

today =date.today()
print(today)
formatted_date =today.strftime("%A-%d-%B-%G")
print(formatted_date)

after_sixty_days = today + timedelta(days=60)
print(after_sixty_days)

dob="1996-08-24"
#convert to date object
date_of_birth= datetime.strptime(dob,"%Y-%m-%d")
age = today.year - date_of_birth.year
print("i am", age, "years")

age_in_days=datetime.today() - date_of_birth
print(age_in_days.days)
