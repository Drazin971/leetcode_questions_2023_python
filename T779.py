class Solution:
  def kthGrammar(self, n: int, k: int) -> int:
    gram = "0"
    while n > 1:
      old_gram = gram
      gram = ""
      for letter in old_gram:
        if letter == "0":
          gram += "01"
        else:
          gram += "10"
        
      n -= 1
      
    return gram[k-1]

sol = Solution()

print(sol.kthGrammar(n = 2, k = 2))  # 1