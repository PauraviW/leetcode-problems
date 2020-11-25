import random
from collections import defaultdict
from datetime import date
from enum import Enum


class Car:
    def __init__(self, color,  modelName, modelNumber, creationYear, rate):
        self.color = color
        self.id = -1
        self.modelName = modelName
        self.modelNumber = modelNumber
        self.creationYear = creationYear
        self.rate = rate
        self.occupied = False
        self.rate = rate

class Account:
    def __init__(self, name):
        self.id = -1
        self.name = name

class Member(Account):
    def __init__(self, name, bill, ownedCar, email):
        super().__init__( name)
        self.bill = bill
        self.ownedCar = ownedCar
        self.email = email
        self.timeRented =date.today()

class Quality(Enum):
    NEW, USED, TOBEDISCARDRD = 1,2,3

class RentalSystem:
    def __init__(self, id):
        self.id = id
        self.cars = defaultdict(list)
        self.modelwiseCare = defaultdict()
        self.budetWise = defaultdict(list)
        self.capacityWise = defaultdict(list)
        self.budgetWisr = defaultdict(list)
        self.members = defaultdict(Member)
        self.mapping = defaultdict(Car)


    def addCar(self, color, id , modelName, modelNumber, creationYear, rate):
        car = Car(color, modelName, modelNumber, creationYear, rate)
        car.id = len(self.cars[modelNumber]) + 1
        self.cars[(modelName,modelNumber)].append(car)

    def deleteCar(self, modelName):
        # if a car is can be deleted or not.

        if self.cars[modelName]:
            car = self.cars.pop()
            self.printMessage(b"Car number: {b} \t Car Model: {a} successfully deleted".format(car.modelName, car.modelNumber))

    def createMember(self, name, email):
        member = Member(name, email)
        self.members[email] = member
        return member

    def rentCar(self,  name, email, modelName):
        if email not in self.members:
            member = self.createMember((name, email))
        else:
            member = self.members[email]
        self.allocateCar(member, modelName)
    def getCar(self, modelName, modelNumber):
        for car in self.cars[(modelName, modelNumber)]:
            if not car.occupied:
                return car
            else:
                return None
        return self.cars[(modelName, modelNumber)]
    def allocateCar(self, member, modelName, modelNumber):
        car = self.getCar(modelName, modelNumber)
        if not car:
            self.printMessage("Sorry, No cars available")
        else:
            member.ownedCar = car
            car.occupied = True
            self.mapping[member] = car
    def billing(self, member, car):
        self.printMessage("The bill is: {a}".format((date.today() - member.timeRented) * car.rate))

    def printMessage(self, msg):
        print(msg)


