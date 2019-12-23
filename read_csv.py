f_r = open('csv_data.txt', 'r')
f = f_r.readlines()
f_r.close()

lines = [line.strip() for line in f[1:]]

header = f[0]
header = header.strip()
header = header.split(', ')
l = list()
for line in lines:
    person_data = line.split(', ')
    d = dict()
    for i in range(len(person_data)):
        d[header[i]] = person_data[i]
    l.append(d)
print(l)