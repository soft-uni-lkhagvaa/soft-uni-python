n = int(input())

current = 1
is_done = False

for row in range(1, n + 1):
  for col in range(1, row + 1):
    if current > n:
      is_done = True
      break
    print(current, end=" ")
    current += 1
  print()
  if is_done:
    break
