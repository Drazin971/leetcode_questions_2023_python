class Solution:
  def largestGoodInteger(self, num: str) -> str:
    largest_int = ""

    for i in range(1, len(num) - 1):
      if num[i-1] == num[i] == num[i+1]:
        if int(num[i-1:i+2]) > int(largest_int):
          largest_int = str(num[i-1:i+2])

    return largest_int

sol=Solution()

print(sol.largestGoodInteger(num = "6777133339")) # 777