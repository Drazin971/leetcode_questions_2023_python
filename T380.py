import random

class RandomizedSet:
    def __init__(self):
      self.randomSet = []
        

    def insert(self, val: int) -> bool:
      if val not in self.randomSet:
        self.randomSet.append(val)
        return True
      else:
        return False
        

    def remove(self, val: int) -> bool:
      if val in self.randomSet:
        self.randomSet.remove(val)
        return True
      else:
        return False
        

    def getRandom(self) -> int:
      return random.choice(self.randomSet)
      
      
      

sol = RandomizedSet()
sol.insert(1)
sol.insert(2)
print(sol.getRandom())