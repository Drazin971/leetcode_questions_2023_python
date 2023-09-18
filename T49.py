class Solution:
  def isAnagram(self, s: str, t: str) -> bool:

      if len(s) != len(t) : return False
        
      for i in range(len(s)):
        t=t.replace(s[i],"*",1)

      return True if t.count("*")==len(t) else False
    
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
      anagrams = []
      while strs:
        current_group = []
        curr_str = strs.pop(0)
        current_group.append(curr_str)
        for item in strs:
          if self.isAnagram(curr_str, item):
            current_group.append(strs.pop(strs.index(item)))
        #print(current_group)
        anagrams.append(current_group)
          
      return(anagrams)
     
    
sol=Solution()

print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])) #Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

print(sol.groupAnagrams(strs = ["","",""])) #Output: [[""]]

print(sol.groupAnagrams(strs = ["",""])) #Output: [[""]]

print(sol.groupAnagrams(strs = ["a"])) #[["a"]]