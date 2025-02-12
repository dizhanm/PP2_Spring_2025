import datetime
x = datetime.datetime.now()
y = x - datetime.timedelta(5)
print(y)
print(f"{y.day}.{y.month}.{y.year}")