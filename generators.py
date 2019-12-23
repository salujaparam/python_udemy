# def hundred():
#     i = 0
#     while i <100:
#         yield i
#         i += 1
# # print(hundred())

# g = hundred()
# print(next(g))
# print(next(g))
# print(list(g))


class FirstHundredGenerator:
    def __init__(self):
        self.number = 0
    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

my_gen = FirstHundredGenerator()
print(next(my_gen))
print(next(my_gen))

class FirstFiveIterations:
    def __init__(self):
        self.numbers = [1,2,3,4,5]
        self.i = 0
    def __next__(self):
        if self.i<len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            return StopIteration()

gen = FirstFiveIterations()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2
 
    def __next__(self):
        for n in range(self.start, self.stop):  # always search from current start (inclusive) to stop (exclusive)
            for x in range(2, n):
                if n % x == 0:      # not prime
                    break
            else:   # n is prime, because we've gone through the entire loop without having a non-prime situation
                self.start = n + 1  # next time we need to start from n + 1, otherwise we will be trapped on n
                return n    # return n for this round
        raise StopIteration()  