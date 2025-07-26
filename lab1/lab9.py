sqMeter = float(input())

une = sqMeter * 7.61
hunglult = une / 100 * 18

finalPrice = une - hunglult

print(f'The final price is: {finalPrice} USD.')
print(f'The discount is: {hunglult} USD.')