class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
      spin = 0 
      ab, bb, cb = bin(a)[2:], bin(b)[2:], bin(c)[2:]
      
      maxL=max(len(ab),len(bb),len(cb))
      
      ab="0"*(maxL-len(ab))+ab
      bb="0"*(maxL-len(bb))+bb
      cb="0"*(maxL-len(cb))+cb
      
      print(ab, bb, cb)
      
      for i in range(len(cb)):
        if int(cb[i])==0:
          spin+=int(ab[i]) + int(bb[i])
        elif (int(ab[i]) + int(bb[i]))==0:
          spin+=1
       
        print(spin)
      
      return(spin)
      


sol = Solution()

print(sol.minFlips(a = 7, b = 7, c = 7))