import sys
from itertools import product, permutations, combinations, combinations_with_replacement

# dice_combinations = product(range(1,7), repeat=2)
# for item in dice_combinations:
#     print(item, end="")

# dice_combi = [(d1, d2) for d1 in range(1,7) for d2 in range(1,7)]
# print(dice_combi)

# l1 = ['a', 'b', 'c']
# l2 = [1, 2, 3]

# cartesian_product = product(l1, l2, repeat=2)
# print('cartesian_product')
# for item in cartesian_product:
#     print(item, end="")

# print(sys.getsizeof(dict()))
# print(sys.getsizeof(list()))
# print(sys.getsizeof(tuple()))


string = "ABC"
print("**********Permutations**********")
perm = permutations(string)
for item in perm:
    print(item)

perm = permutations(string, r=2)
for item in perm:
    print(item)

perm = permutations(string, r=3)
for item in perm:
    print(item)
print("**********Combinations**********")
comb = combinations(string, r=1)
for item in comb:
    print(item)

comb = combinations(string, r=2)
for item in comb:
    print(item)

comb = combinations(string, r=3)
for item in comb:
    print(item)

print("COmbinations with replacement")
comb = combinations_with_replacement(string, r=2)
for item in comb:
    print(item)