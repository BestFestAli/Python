# 1 answer
class Ali():
    def __init__(self):
        pass
    def getString(self):
        self.a = input()
        pass
    def printString(self):
        print(self.a.upper())
        pass
   
ex1 = Ali()     
ex1.getString()
ex1.printString()

# 2 answer
class Shape():
    def area(self):
        return self.lenght * self.width
    
class Square(Shape):
    def __init__(self, lenght = 0):
        self.lenght = lenght
        self.width = lenght

aa = Square(10) 
print(aa.area())

# 3 answer
class Rectangle(Shape):
    def __init__(self, lenght = 0, width = 0):
        self.lenght = lenght
        self.width = width
        
ab = Rectangle(15)
print(ab.area())

# 4 answer
import numpy as np 
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self, idx):
        return self.x[idx], self.y[idx]
    
    def move(self, nx, ny, idx):
        self.x[idx] = nx
        self.y[idx] = ny
        
    def dist(self, idx, jdx):
        return np.sqrt((self.x[idx]-self.x[jdx])**2 + (self.y[idx]-self.y[jdx])**2)
    
plain = Point([0,1,2,3], [0, 1, 4, 9])
print(plain.show(1)) 
print(plain.dist(1, 3))

# 5 answer
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, num):
        self.balance += num
        
    def withdraw(self, num):
        if num <= self.balance:
            self.balance -= num
        else: print("low balance")
    def show(self):
        return self.balance
    
Beka = Account("Beka", 1000)
Beka.deposit(500)
Beka.withdraw(2000)
Beka.deposit(250)
Beka.withdraw(1750)
Beka.show()

# 6 answer
import numpy as np
def prime_filter(nums):
    answer = list(filter(lambda a: (a/b)*b != 0 for b in range(np.sqrt(a)+1), nums))

print(prime_filter([1, 2, 3]))