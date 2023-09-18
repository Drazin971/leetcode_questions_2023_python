from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
      d = deque()
      ans = []
      for i in range(k):
        d.append(nums[i])
        
      for i in range(k, len(nums) - k):
        ans.append(max(d))
        d.popleft()
        d.append(nums[i])
      return ans


sol = Solution()


print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
      d = deque()
      l = r = 0
      ans = []

      while r < len(nums):
        while d and nums[d[-1]] < nums[r]:
          d.pop()
        d.append(r)
        
        if l > d[0]:
          d.popleft()

        if (r+1) >= k:
          ans.append(nums[d[0]])
          l += 1
        r +=1
          
      return ans


sol = Solution()


print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))

print(sol.maxSlidingWindow(nums = [1,-1], k = 1))
        