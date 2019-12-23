# # tuples
# friends = ('param', 'meha')
# friends = friends + ('preyaa',)
# print(friends)

# # sets
# art_friends = {'Rolf', 'Anne'}
# science_friends = {'Jen', 'Charlie'}

# art_friends.add('Jen')
# print(art_friends, science_friends)

# # art_friends.remove('Jen')
# # print(art_friends, science_friends)

# art_but_not_science = art_friends.difference(science_friends)
# print(art_but_not_science)

# science_but_not_art = science_friends.difference(art_friends)
# print(science_but_not_art)

# not_in_both = science_friends.symmetric_difference(art_friends)
# print(not_in_both)

# art_and_science = art_friends.intersection(science_friends)
# print(art_and_science)

# all_friends = art_friends.union(science_friends)
# print(all_friends)

# # dicts

# friends_age = {'Param': 21, 'Meha': 25, 'Preyaa': 23}
# friends_age['Yuvan'] = 22
# print(friends_age.keys())
# print(friends_age.values())
# print(friends_age.items())

# # basic functions sum(--), len(--)

# friends = [('param', 20), ('meha', 24)]
# for friend in friends:
#     name, age = friend
#     print('name is {} and age is {}'.format(name, age))

# friends_ages = {'param': 20, 'meha': 24}
# for name, age in friends_ages.items():
#     print('name is {} age is {}'.format(name, age))

# numbers = [2, 4, 6, 8]

# doubled = [number*2 for number in numbers]
# tripled = numbers*3
# print('numbers -> ', numbers)
# print('doubled -> ', doubled)
# print('tripled -> ', tripled)

# names = ['Param', 'Meha']
# lower = [name.lower() for name in names]
# print(lower)

# ages = [22, 23, 24, 25, 26]

# odds = [age for age in ages if age % 2 == 1]
# print('ages -> ', ages)
# print('odds -> ', odds)

# time_since = [6, 7]

# long_timers = {
#     names[i]: time_since[i]
#     for i in range(len(names))
#     if time_since[i] > 6
# }

# print(long_timers)

# zipp = dict(zip(names, time_since))
# print(zipp)

# divide = lambda x, y: x/y

# print((lambda x,y: x*y)(5,2))

# print(divide(10, 5))

# def gree():
#     print('Hello')

# hello = gree

# hello()

my_student = {
    'name': 'param',
    'grades': [90, 80, 100, 100, 90]
}

def average(student):
    return sum(student['grades'])/ len(student['grades'])

# class Student:
#     def __init__(self, new_name, new_grades):
#         self.name = new_name
#         self.grades = new_grades
#         self.marks = []

#     def average(self):
#         return sum(self.grades)/ len(self.grades)

# student_one = Student('Param', [70, 88, 90, 99])
# print(student_one.name, student_one.average())
# # print(student_one.__class__)

# student_two = Student('Meha', [80, 88, 90, 99])
# print(student_two.name, student_two.average())
# print(student_two.__class__)

# print(Student.average(student_one))

class Garage:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)
    def __getitem__(self, i):
        return self.cars[i]
    def __repr__(self):
        return f'<Garage {self.cars}'
    def __str__(self):
        return f'Garage with {len(self)} cars.'
ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford.cars)
print(len(ford))
# print(ford[0])

for car in ford:
    print(car)

print(ford)

class Student:
    def __init__(self, new_name, school):
        self.name = new_name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/ len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
    
    @property
    def weekly_salary(self):
        return self.salary * 37.5

rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.salary)
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average())
print(rolf.weekly_salary)

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'
    @classmethod
    def from_sum(cls, num1, num2):
        return cls(num1 + num2)
number = FixedFloat(18.5746)
print(number)
new_number = FixedFloat.from_sum(19.575, 0.789)
print(new_number)

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

money = Euro.from_sum(16.758, 9.999)
print(money)