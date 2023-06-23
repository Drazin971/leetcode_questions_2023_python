class SnapshotArray:
    
    def __init__(self, length: int):
      self.array=[0]*length
      self.total_snaps=0
      self.changes = set()
          

    def set(self, index: int, val: int) -> None:
      tup = (index, val)
      if tup[0] in self.changes:
        self.changes.remove(tup[0])
      self.changes.add(tup)
      print(self.changes)
              

    def snap(self) -> int:
      print(self.array, self.array[0])
      self.array.append(self.array)
      self.total_snaps+=1
      return self.total_snaps -1
        

    def get(self, index: int, snap_id: int) -> int:
      return self.array[snap_id+1][index]


snapshotArr = SnapshotArray(3)
#print(snapshotArr.array[0])
snapshotArr.set(0,5)
snapshotArr.snap()
#print(snapshotArr.array[1])
snapshotArr.set(0,6)
print(snapshotArr.array,snapshotArr.array[0],snapshotArr.array[1])
print(snapshotArr.get(0,0))