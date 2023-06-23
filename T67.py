class Solution:
    def addBinary(self, a: str, b: str) -> str:
      result =""
      carry = 0
      while len(a) != len (b):
        if len(a) < len (b):
          a = "0"+a
        else:
          b ="0"+b
      print(a,b)
          
      for i in range(len(a)-1,-1,-1):
        carry = carry + int(a[i]) + int(b[i])
        if carry == 3:
          result = "1" + result
          carry = 1
        elif carry == 2:
          result = "0" + result
          carry = 1
        elif carry == 1:
          result = "1" + result
          carry = 0
        else:
          result = "0" + result
          
      if carry == 1:
        result = "1" + result
      return result
        
          
          

        
sol = Solution()

print(sol.addBinary("11","1"))


          