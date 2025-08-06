import datetime

today = datetime.datetime.today()
date = today.strftime("%Y-%m-%d")
time = today.strftime("%H:%M:%S")

print(f"Today is {date} and it is {time}.")