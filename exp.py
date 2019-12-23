exp = '3 addition 4 multiplication 3 division 3 subtraction 1'

lst = exp.split()

pos_mul = lst.index('multiplication')
div_find = lst.index('division')
add_find = lst.index('addition')
sub_find = lst.index('subtraction')

lst[pos_mul] = '*'
lst[add_find] = '+'
lst[div_find] = '/'
lst[sub_find] = '-'
print(lst)
strr = ''
for item in lst:
    strr = strr + item

print(eval(strr))