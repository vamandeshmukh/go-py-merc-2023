# OOP in Python 
# class object 

# class definiition begins here 
class Employee:

# static field
    salary = 0

# self == this 
# constructor 
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

# static method 
    @classmethod
    def someFun(cls):
        print(cls.salary)
        print('someFun invoked')

# non static method 
    def someFun2(self):
        print(self.firstName, self.lastName)
        print('someFun2 invoked')

# class definiition ends here 

emp = Employee('Sonu', 'Singh')
emp.someFun()
emp.someFun2()

print(emp.salary)


# Other OOP 

class Animal:
    pass

# inheritance 
class Dog(Animal):
    pass
















