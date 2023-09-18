from collections import defaultdict

class Solution:
  def longestArithSeqLength(self, nums: list[int]) -> int:
    n = len(nums)
    if n<2:
      return n
    helper_table = [{} for _ in range(n)]
    longest = 2
    for number in range(n):
      for ar_seq in range(number):
        delta = nums[ar_seq]-nums[number]
        helper_table[number][delta] = helper_table[ar_seq].get(delta,1)+1
        print(helper_table)
        longest = max(longest, helper_table[number][delta])
        
    return longest   

  def longestArithSeqLength2(self, nums: list[int]) -> int:
    dp = defaultdict(dict)
    n = len(nums)
    ans = 1

    for i in range(n):
      for j in range(i):
        diff = nums[i] - nums[j]
        if diff not in dp[j]:
            dp[j][diff] = 1
        if diff not in dp[i]:
            dp[i][diff] = 0
        dp[i][diff] = dp[j][diff] + 1
        print(dp)
        
        ans = max(ans, dp[i][diff])
    
    return ans
     

          
    
sol=Solution()

print(sol.longestArithSeqLength(nums = [3,6,9,12])) #4

print(sol.longestArithSeqLength2(nums = [9,4,7,2,10])) #3, [4,7,10]

#print(sol.longestArithSeqLength(nums = [20,1,15,3,10,5,8])) #4, [20,15,10,5]

#print(sol.longestArithSeqLength(nums = [24,13,1,100,0,94,3,0,3])) #2

#print(sol.longestArithSeqLength(nums = [0,8,45,88,48,68,28,55,17,24])) #2

#print(sol.longestArithSeqLength(nums = [44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28]
#)) #6








