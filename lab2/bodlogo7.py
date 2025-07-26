import math

durs = input()

if durs == 'square':
    a = float(input())
    area = a * a
    print(f"{area:.3f}")
elif durs == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")
elif durs == 'circle':
    r = float(input())
    area = r * r * math.pi
    print(f"{area:.3f}")
elif durs == 'triangle':
    a = float(input())
    h = float(input())
    area = a * h / 2
    print(f"{area:.3f}")
