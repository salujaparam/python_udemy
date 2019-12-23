f_q = open('questions.txt', 'r')
f = f_q.readlines()
f_q.close()
score = 0
total = 0
for line in f:
    line = line.split('=')
    if line[1].endswith('\n'):
        answer = line[1][:-1]
    else:
        answer = line[1]
    answ=input(line[0]+'=')
    if answ==answer:
        score = score+1
        total = total+1
    else:
        total = total+1
    
f_r = open('result.txt', 'w')
f_r.write('Your final score is {}/{}.'.format(score, total))
