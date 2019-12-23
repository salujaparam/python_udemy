import json

with open('friends_json.txt', 'r') as file:
    f = json.load(file)

for data in f['friends']:
    print('name is: ', data['name'], ' degree is: ', data['degree'])


cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

f_w = open('cars_json.txt', 'w')
for car in cars:
    json.dump(car, f_w)

f_w.close()