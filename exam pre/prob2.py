budget = float(input())
nights = int(input())
price_per_night = float(input())
percentage = int(input())

if nights > 7:
  price_per_night *= 0.95

total_cost_of_nights = nights * price_per_night
extra_cost = budget * (percentage / 100)
total_cost = total_cost_of_nights + extra_cost

if budget >= total_cost:
    print(f"Smiths will be left with {budget - total_cost:.2f} USD after vacation.")
else:
    print(f"{total_cost - budget:.2f} USD needed.")