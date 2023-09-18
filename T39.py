class Solution:
  def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
    sol = []
    candidates.sort(reverse=True)
    
    def select(current_sum: int, current_candidates: list[int], i: int):
      if current_sum==target:
        sol.append(current_candidates.copy())
        return
      if current_sum>target or i>=len(candidates):
        return

      current_candidates.append(candidates[i])
      select(current_sum+candidates[i],current_candidates,i)
      current_candidates.pop()
      select(current_sum,current_candidates,i+1)
        
    select(0,[],target)
    
    return sol   

sol = Solution()

r=sol.combinationSum(candidates = [2,3,6,7], target = 7) #[[2,2,3],[7]]

print(r)

r=sol.combinationSum(candidates = [2,3,5], target = 8) #[[2,2,2,2],[2,3,3],[3,5]]

print(r)

r=sol.combinationSum(candidates = [2], target = 1) #[]

print(r)

