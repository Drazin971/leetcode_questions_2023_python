from itertools import starmap

class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
      minimum_cost = float('inf')
      for n in range(len(nums)):  
        current_min = 0
        for item in starmap(lambda x,y: abs(x-nums[n])*y, zip(nums, cost, strict=True)):
          current_min += item
        #print(current_min)
        minimum_cost = min(minimum_cost, current_min)
      return minimum_cost
    
sol=Solution()

print(sol.minCost(nums = [1,3,5,2], cost = [2,3,1,14])) #8 = 2+3+3*1

print(sol.minCost(nums = [2,2,2,2,2], cost = [4,2,8,1,3])) #0

print(sol.minCost(nums = [735103,366367,132236,133334,808160,113001,49051,735598,686615,665317,999793,426087,587000,649989,509946,743518], cost =
[724182,447415,723725,902336,600863,287644,13836,665183,448859,917248,397790,898215,790754,320604,468575,825614])) #1907611126748
