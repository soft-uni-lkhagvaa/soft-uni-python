destination = input()

while not destination == "End":
    minimal_budget = float(input())
    money_saved = 0
    while money_saved < minimal_budget:
        current_money = float(input())
        money_saved += current_money
    print(f"Going to {destination}!")
    destination = input()
