a = input()
day = {"Monday": "Working day", "Tuesday": "Working day", "Wednesday": "Working day", "Thursday": "Working day",
       "Friday": "Working day", "Saturday": "Weekend", "Sunday": "Weekend", }
print(day.get(a, "Error"))
