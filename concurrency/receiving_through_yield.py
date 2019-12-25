# def greet():
#     friend = yield
#     print(f'Hello, {friend}')

# g = greet()
# g.send(None) # Priming the Generator
# g.send('Adam')

from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')

def greet(g):
    # g.send(None)
    # while True:
    #     greeting = yield
    #     g.send(greeting)
    yield from g

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
greeter.send('Hi')