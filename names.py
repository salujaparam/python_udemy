def checker(names):
    first_condition = 0
    second_condition = 0
    for name in names:
        if "at" in name:
            second_condition += 1
        pos = name.find("at")
        if pos == len(name) - 2:
            first_condition += 1
    return first_condition, second_condition

output = checker(["hat", "cat", "rabbit", "matter"])

first = output[0]
second = output[1]
print(first)
print(second)