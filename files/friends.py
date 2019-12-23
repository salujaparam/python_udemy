names = []
for i in range(3):
    x = input(f'friend name {i+1} ')
    names.append(x)

f = open('people.txt', 'r')
f_read = f.readlines()

f_list = []
for line in f_read:
    if line.endswith('\n'):
        line = line[:-1]
    f_list.append(line)
f.close()

f = open('nearby_friends.txt', 'w+')
for i in range(len(names)):
    if names[i] in f_list:
        f.write(names[i]+ '\n')

f.close()