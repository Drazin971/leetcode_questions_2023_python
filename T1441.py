class Solution:
  def buildArray(self, target: list[int], n: int) -> list[str]:
    stack = []
    pos = 0

    for i in range(1,n+1):
      stack.append("push")
      if i == target[pos]:
        pos += 1
      else:
        stack.append("pop")
        
    return stack
    
sol = Solution()

print(sol.buildArray(target = [1,3], n = 3))  # ["Push","Push","Pop","Push"]