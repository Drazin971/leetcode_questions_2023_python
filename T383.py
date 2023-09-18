class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    dict = {}
    for letter in magazine:
      if letter not in dict.keys():
        dict[letter] = 1
      else:
        dict[letter]+=1

    for letter in ransomNote:
      if letter in dict.keys():
        if dict[letter]>0:
          dict[letter]-=1
        else: 
          return False
      else:
        return False
    return True
      
    
    
    
     
    
sol=Solution()

print(sol.canConstruct(ransomNote = "aa", magazine = "ab")) #0

print(sol.canConstruct(ransomNote = "aa", magazine = "aab")) #1