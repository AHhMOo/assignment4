temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]


second_week = temperatures[7:15]

print("Second week temperatures:", ", ".join(map(str, second_week)))


above_100 = []

for temp in temperatures:
    if temp > 100:
        above_100.append(temp)

print("Temperatures above 100:", ", ".join(map(str, above_100)))
