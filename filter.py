# def starts_with_p(friend):
#     return friend.startswith('P')

friends = ['Param', 'Meha', 'Prachi', 'Anna', 'Medha']

# start_with_p = filter(starts_with_p, friends)
start_with_p = filter(lambda friend: friend.startswith('P'), friends)

# print(next(start_with_p))
# print(next(start_with_p))

# print(list(start_with_p))

names = [name for name in start_with_p]
print(names)

another_starts_with_p = (f for f in friends if f.startswith('P'))
for f in another_starts_with_p:
    print(f)

def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i

l = my_custom_filter(lambda x: x.startswith('M'), friends)
print(next(l))
print(next(l))