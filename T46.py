class Solution:
  def permute(self, nums: list[int]) -> list[list[int]]:
    sol = []
    ans = len(nums)

    def find_permutations(possible: list[int], num: int) -> list:
      if len(possible)==ans:
        sol.append(possible.copy())
        return 
      for i in range(ans):
        if nums[i] not in possible:
          possible.append(nums[i])
          find_permutations(possible,num+1)
          possible.pop()
      
    find_permutations([],0)

    return sol
      

sol = Solution()

r=sol.permute(nums = [1,2,3]) #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

print(r)

r=sol.permute(nums = [0,1]) #[[0,1],[1,0]]

print(r)

r=sol.permute(nums = [1]) #[[1]]

print(r)