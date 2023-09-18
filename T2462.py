class Solution:
  def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
    total_cost = 0
    for _ in range(k):
      if len(costs) < candidates*2:
        candidate = min(costs)
      else:
        candidate = min(costs[:candidates] + costs[-candidates:]) #<- tutaj
      print(total_cost, candidate, costs)
      total_cost += costs.pop(costs.index(candidate))
    return total_cost
    
sol=Solution()

"""#print(sol.totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4)) #11

#print(sol.totalCost(costs = [1,2,4,1], k = 3, candidates = 3)) #4]

print(sol.totalCost(costs =
[50,80,34,9,86,20,67,94,65,82,40,79,74,92,84,37,19,16,85,20,79,25,89,55,67,84,3,79,38,16,44,2,54,58], k = 11, candidates =2)) #423"""

print(sol.totalCost(costs =
[50,80,34,9,86,20,67,94,65,82,40,79,74,92,84,37,19,16,85,20,79,25,89,55,67,84,3,79,38,16,44,2,54,58], k = 7, candidates =12)) #95

import heapq

class Solution:
  def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
    total_cost = 0
    heap = []
    l, r = 0, len(costs) - 1

    #print(len(costs))

    for i in range(candidates):
      if not heap or l<r-2:
        #print(i, l, r, costs[i], costs[len(costs)-1-i])
        heapq.heappush(heap, (costs[i],i))
        l =  i
        heapq.heappush(heap, (costs[len(costs)-1-i],len(costs)-1-i))
        r = len(costs)-1-i

    
    while k>0:
      val, ind  = heapq.heappop(heap)

      #print(val, ind)
      
      if ind <= l and l+1<r:
        l+=1
        heapq.heappush(heap, (costs[l],l))
      elif ind >= r and r-1>l:
        r-=1
        heapq.heappush(heap, (costs[r],r))
        
      
      total_cost += val
      k -= 1
    
    return total_cost
    
sol=Solution()

print(sol.totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4)) #11

print(sol.totalCost(costs = [1,2,4,1], k = 3, candidates = 3)) #4]

print(sol.totalCost(costs =
[50,80,34,9,86,20,67,94,65,82,40,79,74,92,84,37,19,16,85,20,79,25,89,55,67,84,3,79,38,16,44,2,54,58], k = 11, candidates =2)) #423

print(sol.totalCost(costs =
[50,2,34,9,86,20,67,94,65,82,40,79,74,92,84,37,19,16,85,20,79,25,89,55,67,84,3,79,38,16,44,2,54,58], k = 7, candidates =12)) #95


print(sol.totalCost(costs =
[18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75], k = 13, candidates =23)) #223



