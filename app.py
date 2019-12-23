f = open('data.txt', 'r')
f_content = f.read()
f.close()
print(f_content)

name = input('Enter your name: ')
f_write = open('data.txt', 'w')
f_write.write(name)
f_write.close()
