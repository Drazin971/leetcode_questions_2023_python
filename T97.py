class Solution:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

    if len(s1+s2) != len (s3): return False
    
    memo = {}

    def dfs(is1, is2):
      if (is1 == len(s1)) and (is2 == len(s2)): 
        return True
      if (is1,is2) in memo:
        return memo[(is1, is2)]
      
      if is1<len(s1) and s1[is1] == s3[is1+is2] and dfs(is1+1,is2):
          memo[(is1,is2)]=True
          return memo[(is1,is2)]

      if is2<len(s2) and s2[is2] == s3[is1+is2] and dfs(is1,is2+1):
          memo[(is1,is2)]=True
          return memo[(is1,is2)]

      memo[(is1,is2)]=False
      return False
  
    return dfs(0,0)
      
    
sol = Solution()

print(sol.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac")) #True

print(sol.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc")) #False

print(sol.isInterleave(s1 = "", s2 = "", s3 = "")) #True