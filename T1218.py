
class Solution:
  def longestSubsequence(self, arr: list[int], difference: int) -> int:
    seq = {}

    for val in arr:
        seq[val] = seq.get(val - difference, 0) + 1
    return max(seq.values())

sol = Solution()

r=sol.longestSubsequence(arr = [1,3,5,7], difference = 1) #1

print(r)

r=sol.longestSubsequence(arr = [1,2,3,4], difference = 1) #4

print(r)

r=sol.longestSubsequence(arr = [1,5,7,8,5,3,4,2,1], difference = -2) #4

print(r)
