class Node:
  def __init__(self, key=-1, val=-1, next=None):
    self.key = key
    self.val = val
    self.next = next
    

class MyHashMap:

    def __init__(self):
      self.hmap = [Node() for i in range(23)]
        
    def hash(self, key):
      return key % 23
        

    def put(self, key: int, value: int) -> None:
      self.key = self.hash(key)
      cur = self.hmap[self.key]
      while cur.next:
        if cur.next.key == key:
          cur.next.val = value
          return
        cur = cur.next
      cur.next = Node(key, value)
      
        

    def get(self, key: int) -> int:
      self.key = self.hash(key)    
      cur = self.hmap[self.key].next
      while cur:
        if cur.key == key:
          return cur.val
        cur = cur.next
      return -1

    def remove(self, key: int) -> None:
      self.key = self.hash(key)  
      cur = self.hmap[self.key]
      while cur and cur.next:
        if cur.next.key == key:
          cur.next = cur.next.next
          return
        cur = cur.next