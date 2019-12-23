names = ['Param', 'Meha', 'Preyaa', 'Yuvan']

# friends_lower = map(lambda x: x.lower(), names)
friends_lower = [friend.lower() for friend in names]
# friends_lower = (friend.lower() for friend in names)
# print(next(friends_lower))
print(friends_lower)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    # @classmethod
    # def from_dict(cls, data):
    #     return cls(data['username'], data['password'])

users = [
    {'username': 'param', 'password': '123'},
    {'username': 'preti', 'password': '246'}
]

# users = [User(data['username'], data['password']) for data in users]
# print(users)

users = [User(**data) for data in users]
print(users)

# users1 =  map(User.from_dict, users)
# print(users1)

userss = [
    ('rolf', '123'),
    ('param', '246')
]

usersss = [User(*data) for data in userss]
print(usersss)