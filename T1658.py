class Solution:
  def minOperations(self, nums: list[int], x: int) -> int:

    sol = float('inf')

    def dfs(l, r, sum):
      nonlocal sol
      if sum==x:
        sol = min(sol, len(nums) - l  - r - 1) 
        return
      if l<r:
        dfs(l+1,r,sum+nums[l])
        dfs(r-1,sum+nums[r])

    dfs(0,len(nums)-1,0)

    return sol

sol = Solution()

print(sol.minOperations(nums = [3,1,3,4,2])) #2