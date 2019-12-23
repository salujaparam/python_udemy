import json
f_r = open('csv_file.txt', 'r')
f = f_r.readlines()
f_r.close()

l = list()
for line in f:
    line = line.strip()
    line = line.split(',')
    d = dict()
    d['club']=line[0]
    d['country']=line[1]
    d['city']=line[2]
    l.append(d)
    
f_w = open('json_file.txt', 'w')
json.dump(l, f_w)
f_w.close()