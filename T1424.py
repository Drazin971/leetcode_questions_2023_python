class Solution:
  def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
    res = []
    c = max(len(nums), len(max(num for num in nums)))

    for x in range(c):
      for row in range(x,-1,-1):
          col = x - row
          try:
            res.append(nums[row][col])
          except:
            continue

    for x in range(c):
      row = c
      for col in range(x+1,c+1):
          row -= 1
          try:
            res.append(nums[row][col])
          except:
            continue

    return res

sol=Solution()

print(sol.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])) # [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

print(sol.findDiagonalOrder([[6],[8],[6,1,6,16]])) 