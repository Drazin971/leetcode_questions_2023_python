class Solution:
    def search(self, nums: list[int], target: int) -> int:
      return nums.index(target) if target in nums else -1

    def search(self, nums: list[int], target: int) -> int:
      start, end = 0, len(nums)-1
      while start<=end:
        mid = start+(end-start)//2
        if nums[mid]==target: return mid
        
        if nums[start]<=nums[mid]:
            if nums[start]<=target<=nums[mid]:
                end = mid-1
            else:
                start = mid+1
        else:
            if nums[mid]<=target<=nums[end]:
                start = mid+1
            else:
                end = mid-1

      return -1
      

sol=Solution()

r=sol.search(nums = [4,5,6,7,0,1,2], target = 0) #4

print(r)

r=sol.search(nums = [4,5,6,7,0,1,2], target = 3) #-1

print(r)

r=sol.search(nums = [1], target = 0) #-1

print(r)