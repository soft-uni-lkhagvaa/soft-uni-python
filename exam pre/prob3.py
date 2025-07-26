budget = float(input())
destination = input()
season = input()
days = int(input())

price_per_day = 0

if destination == "Dubai":
  if season == "Winter":
    price_per_day = 45000
  else:
    price_per_day = 40000
elif destination == "Washington":
  if season == "Winter":
    price_per_day = 17000
  else:
    price_per_day = 12500
elif destination == "London":
  if season == "Winter":
    price_per_day = 24000
  else:
    price_per_day = 20250

total_cost = price_per_day * days

if destination == "Dubai":
  total_cost = total_cost * 0.7
elif destination == "Washington":
  total_cost = total_cost * 1.25

if budget >= total_cost:
  print(f"The budget for the movie is enough! We have {budget - total_cost:.2f} USD left!")
else:
  print(f"The director needs {total_cost - budget:.2f} USD more!")