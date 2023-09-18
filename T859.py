class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
      if len(s) != len(goal):
        return False

      comp = []
      double = False
      
      for i in range(len(s)):
        if s[i] != goal[i]:
          comp.append([s[i],goal[i]])
        else:
          if s.count(s[i]) == goal.count(s[i]) and s.count(s[i])>1:
            double = True

      #print(comp)
      
      if len(comp)==2 and comp[0][0]==comp[1][1] and comp[0][1]==comp[1][0]:
        return True
      elif len(comp)==0:
        if double==True:
          return True
        else: 
          return False
      else:
        return False
      
     
        


sol=Solution()

print(sol.buddyStrings(s = "ab", goal = "ba")) 
print(sol.buddyStrings(s = "abc", goal = "bac")) 
print(sol.buddyStrings(s = "ab", goal = "ab")) 
print(sol.buddyStrings(s = "ab", goal = "ca")) 
print(sol.buddyStrings(s = "abcaa", goal = "abcbb")) 










 



