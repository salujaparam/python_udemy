inp = input()
inp = inp.split(' ')

l = list()
for i in inp:
    num = int(i)
    l.append(i)
s = sum(l) + 1
print(s)