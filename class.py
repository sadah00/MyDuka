class person:
    def __init__(self, name,):
        self.name = name

obj1=person("Alice")
print(obj1.name)

# create a bankaccount class have a constructor to initialize the account with the account number, balance,owner name
# have the methods:
# 1. deposit()
# 2. withdraw()
# 3. display_info()
# create 2 bankaccounts that can deposit,withdraw and display info

class BankAccount:
    def __init__(self,account_number,balance,owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
        else:
         print("Invalid deposit amount")

    def withdraw(self,amount):
        if amount > 0:
            if self.balance <= amount:
                print("Insufficient balance")
            else:
                self.balance-=amount
        else:
            print("Invalid withdraw sum")

    def display_info(self):
        print(f"Account Number: {self.account_number} Balance: {self.balance} Owner: {self.owner}")

bank1 = BankAccount("3434",2000,"John")
bank2 = BankAccount("5789",50000,"Mark")
bank1.deposit(2000)

bank1.display_info()
bank2.display_info()

# Create a student class with the following attribures
# 1.student_id
# 2.name 
# 3.email 
# 4.course
# it should have the following methods:
# 1. enroll_course
#  2. drop_course() 
# 3.set_grade() 
# 4. display_info()
# Create 2 student objects who can do all of the above

class Student:
    def __init__(self,student_id,name,email,course,grade=""):
        self.student_id=student_id
        self.name=name
        self.email=email
        self.course=course
        self.grade=grade

    def enroll_course(self,course):
        self.course = course

    def drop_course(self):
        self.course = ""

    def set_grade(self,course,grade):
        self.course = course
        self.grade = grade

    def display_info(self):
        print(f"Student ID: {self.student_id} Name: {self.name} Email: {self.email} Courses: {self.course} Grade : {self.grade}")

std1=Student(1234,"Bridge","bridge11@gmail.com","Web Development")
std2=Student(5678,"Faith","faith22@gmail.com","Data Science")

std1.enroll_course("Art")
std1.drop_course()
std2.set_grade("Science","A")

std1.display_info()
std2.display_info()


# Create a Car Class
# Have the following attributes
# - brand - model - yer -fuel_capcity - fuel_level -is_running(boolen value)
# Have the methods
# - start()
# - stop()
# - refuel()
# - drive()
# - display_car_info()
class Car:
    def __init__(self,brand,model,year,fuel_capacity,fuel_level=0,is_running=False):
        self.brand=brand
        self.model=model
        self.year=year
        self.fuel_capacity=fuel_capacity
        self.fuel_level=fuel_level
        self.is_running=is_running

    def start(self):
        if self.is_running:
            self.is_running=True
            print("Car started")
       
    def stop(self):
        if self.is_running:
            self.is_running=False
            print("Car stopped")
       
    def refuel(self,amount):
        if amount>0:
            if self.fuel_level + amount <= self.fuel_capacity:
                self.fuel_level += amount
                print(f"Car refueled by {amount} liters")
            else:
                print("Fuel exceeds capacity")
        else:
            print("Invalid fuel amount")

    def drive(self,distance):
        if self.is_running:
            fuel_needed = distance / 10
            if self.fuel_level >= fuel_needed:
                self.fuel_level -= fuel_needed
                print(f"Car drove {distance} km")
            else:
                print("Not enough fuel to drive")
        else:
            print("Start the car first")

    def display_car_info(self):
        print(f"Brand: {self.brand} Model: {self.model} Year: {self.year} Fuel Capacity: {self.fuel_capacity} liters Fuel Level: {self.fuel_level} liters Is Running: {self.is_running}")

machine1=Car("Toyota","Corolla",2020,50,20,False)
machine2=Car("Honda","Civic",2019,45,10,True)

machine1.refuel(30)
machine1.start()
machine2.stop()
machine1.drive(30)

machine1.display_car_info()
machine2.display_car_info()