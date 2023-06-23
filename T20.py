class Solution:
  def isValid(self, s: str) -> bool:
    list_of_open_brackets = ["{","[","("]
    list_of_brackets = {
      "{":"}",
      "[":"]",
      "(":")"
    }
  
    tempSol = ""

    for i in range(len(s)):
      if s[i] in list_of_open_brackets:
        tempSol += s[i]
      elif tempSol=="":
        return False
      elif s[i] == list_of_brackets[tempSol[-1]]:
        tempSol = tempSol[:-1]
      else:
        return False

    if tempSol == "":
      return True   
    else: 
      return False
  
sol = Solution()

print(sol.isValid("}"))
    