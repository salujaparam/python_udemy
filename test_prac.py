# import math
# # n = input('Enter number')
# # try:
# #     n = int(n)
# # except:
# #     print('Taking n as 5 as you have not entered a valid integer')
# #     n = 5
# # d = dict()
# # for i in range(n):
# #     j = i+1
# #     d[j] = j*j

# # print(d)

# n = input('Enter number')
# try:
#     n = int(n)
# except:
#     print('Taking n as 5')
#     n = 5
# l = list()
# for i in range(n):
#     n = int(input('Enter a number'))
#     l.append(n)
# print(l)
# t = tuple(l)
# print(t)
# s = math.sqrt(4)
# print(s)


inp = input()

str1 = inp

mid = len(str1)//2
n = len(str1)-1
x = 0
li = list()
for i in range(len(str1)):
    if x!=mid:
        count = mid-i
    elif x==mid:
        count = 0
    elif x>mid:
        count = i-mid
    l = ''
    l = l + str1[i]
    while count!=0:
        l = l + ' '
        count = count-1
    l = l + str1[n-i]
    x = x+1
    li.append(l)
print(li)

