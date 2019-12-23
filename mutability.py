friends = {
    'param': 10,
    'jen': 13,
    'anna': 16
}

print(id(friends))

friendss = {
    'param': 10,
    'jen': 13,
    'anna': 16
}

print(id(friendss))

friendsss = friendss
print(id(friendsss))

# Immutable -> floats, integers, strings, tuples
# Mutable -> Lists

frien = ['Param', 'Meha']
print(id(frien))

frien.append('Preyaa')
print(id(frien))