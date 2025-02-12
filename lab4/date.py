#1 task
import datetime

cur_date = datetime.datetime.now()

five_days_ego = cur_date - datetime.timedelta(days=5)

print(five_days_ego)

#2 task
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tommorow = today + datetime.timedelta(days=1)

print(yesterday.strftime("%Y-%B-%d"))
print(today.strftime("%Y-%B-%d"))
print(tommorow.strftime("%Y-%B-%d"))

#3 task
cur_date = datetime.datetime.now()
print(cur_date.replace(microsecond=0))

#4 task
firstdate = datetime.datetime(2025, 2, 12, 0, 0, 25)
seconddate = datetime.datetime(2025, 2, 12, 0, 0, 0)
print(abs(firstdate - seconddate).total_seconds())