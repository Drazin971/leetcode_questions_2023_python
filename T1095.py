# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
  def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

    l = 0
    r = mountain_arr.length() - 1

    while l <= r:
      m = l + (r - l) // 2
      if mountain_arr.get(m) < mountain_arr.get(m+1):
        l = m + 1
      else:
        r = m - 1

    peak = m

    if mountain_arr.get(peak) == target:
      return peak

    l = 0
    r = peak 

    while l <= r:
      m = l + (r - l) // 2
      if mountain_arr.get(m) < target:
        l = m + 1
      elif mountain_arr.get(m) > target:
        r = m - 1
      else:
        return m

    l = peak
    r = mountain_arr.length() - 1

    while l <= r:
      m = l + (r - l) // 2
      if mountain_arr.get(m) > target:
        l = m + 1
      elif mountain_arr.get(m) < target:
        r = m - 1
      else:
        return m

    return -1  
