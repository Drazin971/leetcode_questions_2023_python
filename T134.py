class Solution:
  def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
    if sum(gas)<sum(cost):
      return -1
    else:
      answer, amount_gas = 0,0
      for idx,(g,c) in enumerate(zip(gas, cost)):
       print(idx,g,c,amount_gas)
       amount_gas += g-c
       if amount_gas < 0:
         amount_gas =0
         answer=idx+1
      return answer
           
       

sol=Solution()

print(sol.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2])) #3
print(sol.canCompleteCircuit(gas = [5,8,2,8], cost = [6,5,6,6])) #3
