friends = [
    {
        'name': 'Param',
        'location': 'Chennai'
    },
    {
        'name': 'Meha',
        'location': 'Bengaluru'
    },
    {
        'name': 'Preyaa',
        'location': 'Karanataka'
    },
    {
        'name': 'Yuvan',
        'location': 'Delhi'
    }
]

your_location = input('Where are you from?')

friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):
    print('You are not alone...')
    
print(all([1,2,3,4,5]))
print(all([1,2,3,4,0]))