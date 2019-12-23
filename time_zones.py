from datetime import datetime, timezone, timedelta

# print(datetime.now())
# print(datetime.now(timezone.utc))

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)
print(today)
print(tomorrow)

print(today.strftime('%d-%m-%y %H:%M:%S'))

# user_date = input("Enter date in YYYY-mm-dd format")
# user_date = datetime.strptime(user_date, '%Y-%m-%d')

# print(user_date)

import time
import timeit

def power(limit):
    return [x**2 for x in range(limit)]

start = time.time()
print(power(500000))
end = time.time()

print(end-start)

print(timeit.timeit("[x**2 for x in range(10)]"))