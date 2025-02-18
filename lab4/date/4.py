import datetime

x = datetime.datetime(2020, 5, 17, 12, 45, 45)
y = datetime.datetime(2026, 3, 23, 23, 34, 21)

z = abs(x - y)

print(int(z.total_seconds()))