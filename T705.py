class MyHashSet:

    def __init__(self):
      self.hashKey = []
        

    def add(self, key: int) -> None:
      if key not in self.hashKey:
        self.hashKey.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.hashKey:
          self.hashKey.remove(key)

    def contains(self, key: int) -> bool:
       if key in self.hashKey:
         return True
       else:
         return False

myHashSet = MyHashSet()
print(myHashSet.add(1))
print(myHashSet.add(2))
print(myHashSet.contains(1))
print(myHashSet.contains(3))
print(myHashSet.add(2))
print(myHashSet.contains(2))
print(myHashSet.remove(2))
print(myHashSet.hashKey)