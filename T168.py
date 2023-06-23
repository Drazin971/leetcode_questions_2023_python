lass Solution:
    def titleToNumber(self, columnTitle: str) -> int:
    
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter)-64
            ans += digit * 26**pos
            pos += 1
            
        return ans
      

sol = Solution()

print(sol.titleToNumber("FXSHRXW"))

#2147483647

print(sol.titleToNumber("ABA"))

