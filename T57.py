class Solution:
   def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    intervals.append(newInterval)
    intervals = sorted(intervals)
    merged = []
    
    for interval in intervals:
      if not merged or interval[0]>merged[-1][1]:
        merged.append(interval)
      else:
        merged[-1][1]=max(merged[-1][1],interval[1])
    return merged
      
  
 

sol=Solution()

print(sol.insert(intervals = [[1,3],[6,9]], newInterval = [2,5])) #[[1,5],[6,9]]

print(sol.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])) #[[1,2],[3,10],[12,16]]