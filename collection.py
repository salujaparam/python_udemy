"""
* counter
* defaultfict
* ordereddict
* namedtuple
* deque
"""

from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

device_temp = [13.5, 14, 14.5, 14.5, 15.0, 16.0]

temp_counter = Counter(device_temp)
print(temp_counter)

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

aa = defaultdict(list)

for coworker, place in coworkers:
    aa[coworker].append(place)

aa.default_factory = int
print(aa['Rolf'])
print(aa['Anne'])

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o)

o.move_to_end('Rolf')
o.move_to_end('Jen', last=False)

print(o)

o.popitem()

print(o)

account = ('checking', 1850.90)

print(account[0])
print(account[1])

Account = namedtuple('Account', ['name', 'balance'])

account = Account('checking', 1850.90)
print(account.name)
print(account.balance)
print(account)

friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))

print(friends)

friends.append('Jose')
friends.appendleft('Anthony')

print(friends)

friends.pop()
friends.popleft()

print(friends)