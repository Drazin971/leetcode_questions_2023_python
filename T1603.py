class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
      self.big = big
      self.medium = medium
      self.small = small
        

    def addCar(self, carType: int) -> bool:
      if carType == 1:
        if self.big > 0:
          self.big -=1
          return True
        else:
          return False
      if carType == 2:
        if self.medium > 0:
          self.medium -=1
          return True
        else:
          return False
      if carType == 3:
        if self.small > 0:
          self.small -=1
          return True
        else:
          return False

parking = ParkingSystem(1,1,0)
print(parking.addCar(1))
print(parking.addCar(1))
print(parking.addCar(2))
print(parking.addCar(3))
print(parking.addCar(1))

          
