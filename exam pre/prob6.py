start = input()
end = input()

# for num in range(start, end + 1):
#   is_valid = True
#   for digit in str(num):
#     if int(digit) % 2 == 0:
#       is_valid = False
#       break
#   if is_valid:
#     print(num, end=" ")

for d1 in range(int(start[0]), int(end[0]) + 1):
  for d2 in range(int(start[1]), int(end[1]) + 1):
    for d3 in range(int(start[2]), int(end[2]) + 1):
      for d4 in range(int(start[3]), int(end[3]) + 1):
        if all(int(d) % 2 != 0 for d in [d1, d2, d3, d4]):
          print(f"{d1}{d2}{d3}{d4}", end=" ")
