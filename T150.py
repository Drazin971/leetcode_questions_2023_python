class Solution:
  def hIndex(self, citations: list[int]) -> int:
    current_max=0
    for i in range(1,len(citations)+1):
      hsum=sum(1 for item in citations if item>=i) 
      if hsum>=i:
       current_max=max(current_max,i)
      
    return current_max
      
      

sol = Solution()

print(sol.hIndex(citations = [1]))

class Solution:
  def evalRPN(self, tokens: list[str]) -> int:
    result = []
    for item in tokens:
      if item.isdecimal() or item[1:].isdecimal(): #<-
        result.append(item)
      else:
        op1 = result.pop()
        op2 = result.pop()
        #print(op1,op2,item)
        score = int(eval(str(op2) + " " + item + " " + str(op1)))
        result.append(score)
        #print(score, result)
    return result[0]


sol=Solution()

print(sol.evalRPN(tokens = ["2","1","+","3","*"])) #9

print(sol.evalRPN(tokens = ["4","13","5","/","+"])) #6

print(sol.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) #22

print(sol.evalRPN(tokens = ["18"])) #18