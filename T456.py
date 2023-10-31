from collections import deque

class Solution:
  def find132pattern(self, nums: list[int]) -> bool:
    n = len(nums)

    stack = deque()

    max_third_number = float("-inf")

    for i in range(n-1,-1,-1):
      if nums[i] <  max_third_number:
        return True
      while stack and stack[0]<nums[i]:
        max_third_number = stack.popleft()
      stack.appendleft(nums[i])
          
    return False
      

sol = Solution()

print(sol.find132pattern(nums = [1,0,1,-4,-3])) 