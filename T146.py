class LRUCache:
  def __init__(self, capacity: int):
    self.cache={}
    self.capacity = capacity
    self.oldest = 1

  def delete_oldest(self):
    min_age = float("inf")
    for key, item in self.cache.items():
      if item[1]<min_age:
        min_age=item[1]
        min_key=key
    self.cache.pop(min_key)
    
  def get(self, key: int) -> int:
    if key in self.cache.keys():
      self.cache[key][1]=self.oldest
      self.oldest+=1
      return self.cache[key][0]
    else:
      return -1
        

  def put(self, key: int, value: int) -> None:
    if len(self.cache.keys()) == self.capacity and key not in self.cache.keys():
      self.delete_oldest()
    self.cache[key]=[value,self.oldest]
    self.oldest+=1
     
  def print_LRU(self) -> None:
    for item in self.cache.items():
      print (item)
  

LRU=LRUCache(2)
print(LRU.put(1, 1))
print(LRU.put(2, 2))
print(LRU.get(1))
print(LRU.put(3, 3))
print(LRU.get(2))
print(LRU.put(4, 4))

#LRU.print_LRU()

print(LRU.get(1))
print(LRU.get(3))
print(LRU.get(4))

#LRU.print_LRU()
