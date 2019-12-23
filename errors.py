# IndexError          -> out of range
# KeyError            -> when the key called is not present in the dict
# NameError           -> When the variable used is not defined
# AttributeError      -> when the attribute used on a particular structure doest not exist
# NotImplementedError -> The feature not been implemented yet
# RuntimeError        -> Other errors extend from this and occurs when you run your program
# SyntaxError         -> having an illegal syntax
# IndentationError    -> having indentation syntax error
# TabError            -> error when switching between editors, mix and match of spaces and tabs
# TypeError           -> using different types of variables for a particular operation
# ValueError          -> converting a string '20.5' to an int
# ImportError         -> import one file which imports the same file, a circular import
# DeprecationWarning  -> no longer the best way to do something

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)
    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"Tried to add a '{car.__class__.__name__}' to the garage, but you can only add 'Car' objects.")
        self.cars.append(car)

ford = Garage()
car = Car('Ford', 'Fiesta')
ford.add_car(car)
print(len(ford))