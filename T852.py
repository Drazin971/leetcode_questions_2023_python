class Solution:
  def peakIndexInMountainArray(self, arr: list[int]) -> int:

    lo, hi = 0, len(arr)-1

    while lo<hi:
      mid = lo + (hi - lo) // 2
      if arr[mid-1] < arr[mid] > arr[mid+1]: return mid

      if arr[lo] < arr[mid]:
        if arr[mid]>arr[mid-1]:
          lo = mid
        else: 
          hi = mid
      else:
        hi = mid 
      
sol=Solution()

r=sol.peakIndexInMountainArray(arr = [24,69,100,99,79,78,67,36,26,19]) # 2

print(r)

r=sol.peakIndexInMountainArray(arr = [10,9,2,1,0]) #1

print(r)

r=sol.peakIndexInMountainArray(arr = [0,1,2,3,10,5,2]) # 1

print(r)