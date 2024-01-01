class Solution:
  def minOperations(self, s: str) -> int:

    zs, os = 0, 0 

    for i in range(len(s)):
      if i % 2 == 0:
        if s[i] == "0":
            os += 1
        else:
            zs += 1
      else:
        if s[i] == "1":
            os += 1
        else:
            zs += 1

    return  min(zs, os)

sol=Solution()

print(sol.minOperations(s = "1111"))