import enum
import time
from collections import defaultdict


class VehicleEnum(enum.Enum):
    Bus = 1
    Car = 2
    Electric = 3
class ParkingLot:
    def __init__(self):
        pass

class Vehicle:
    def __init__(self, vehicleType, vehicleId, color):
        self.vehicleType = vehicleType
        self.vehicleId = vehicleId
        self.color = color

    def getVehicle(self):
        vehicle = self.vehicleType
        return vehicle
class Bus(Vehicle):
    def __init__(self, vehicleType, vehicleId, color, rate):
        super().__init__(self, vehicleType,vehicleId, color)
        self.rate = rate

class Electric(Vehicle):
    def __init__(self, vehicleType, vehicleId, color, rate, hours):
        super().__init__(self, vehicleType,vehicleId, color)
        self.rate = rate
        self.hours = hours

class ParkingSlot:
    def __init__(self, id, type, status, vehicle):
        self.id = id
        self.type = type
        self.timeStart = time.now()
        self.status = status
        self.rate = 100
        self.vehicleNo = vehicle

class ParkingLot:
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity
        self.EmptyParkingSpots = set()
        self.parkingDict = defaultdict(ParkingSlot)
    def park(self, vehicleNo, type, color):

        if self.capacity > 0:
            slotId = self.getEmptySlot()
            slot = ParkingSlot(slotId, type, Vehicle( vehicleNo, color, type))
            self.parkingDict[slotId] = slot
            self.capacity -= 1




    def getEmptySlot(self):
        for i in range(self.capacity):
            if i in self.EmptyParkingSpots:
                return i





