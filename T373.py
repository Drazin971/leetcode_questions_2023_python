class Solution:
  def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    list_of_pairs=[]
    pointer_a, pointer_b = 0, 0 
    for _ in range(k):
      list_of_pairs.append([nums1[pointer_a],nums2[pointer_b]])
      if nums1[pointer_a+1]<nums1[pointer_b+1] and pointer_a<len(nums1):
        pointer_a += 1
      elif pointer_b < len(nums2): 
        pointer_b += 1
                                                
    return list_of_pairs

sol=Solution()

print(sol.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3)) #[[1,2],[1,4],[1,6]]

print(sol.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2)) #[[1,1],[1,1]]

print(sol.kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3)) #[[1,3],[2,3]]


import heapq

class Solution:
  def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:

    nums = []
    visited = set()

    def generate_pairs():
      for i in nums1:
        for j in nums2:
          yield [i,j]

    pairs_genarator = generate_pairs()

    for _ in range(min(k,len(nums1)*len(nums2))):
      pair = next(pairs_genarator)
      if tuple(pair) not in visited:
        visited.add(tuple(pair))
        heapq.heappush(nums,pair)
    
    heapq.heapify(nums)
    
    for pair in pairs_genarator:
      if tuple(pair) not in visited and pair[0]+pair[1]<nums[0][0]+nums[0][1]:
          heapq.heappop(nums)
          heapq.heappush(nums, pair)
          visited.add(tuple(pair))
    
    return nums
    
      
sol=Solution()

r=sol.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3) # [[1,2],[1,4],[1,6]]

print(r)

r=sol.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2) # [[1,1],[1,1]]

print(r)

r=sol.kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3) # [[1,3],[2,3]]

print(r)

import heapq

class Solution:
  def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:

    nums = [[nums1[0]+nums2[0],0,0]]
    ans = []
    visited = set()

    while k and nums:
      _, i, j = heapq.heappop(nums)
      ans.append([nums1[i],nums2[j]])
      k -= 1

      next = i + 1

      if next < len(nums1) and (next, j) not in visited:
        visited.add((next, j))
        heapq.heappush(nums, [nums1[next]+nums2[j], next, j])

      next = j + 1
      
      if next < len(nums2) and (i, next) not in visited:
        visited.add((i, next))
        heapq.heappush(nums, [nums2[next]+nums1[i], i, next])
      
    return ans
    
      
sol=Solution()

r=sol.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3) # [[1,2],[1,4],[1,6]]

print(r)

r=sol.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2) # [[1,1],[1,1]]

print(r)

r=sol.kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3) # [[1,3],[2,3]]

print(r)





