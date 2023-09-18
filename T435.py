class Solution:
  def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
    intervals.sort()
    end = intervals[0][1]
    ans = 0 

    print(intervals)
    
    for interval in intervals[1:]:
      curr_start, curr_end = interval
      if curr_start>=end:
        end=curr_end
      else: 
         ans+=1
         end=min(curr_end, end) 
    return ans 

sol = Solution()

r=sol.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]) #[[2,2,3],[7]]

print(r)

r=sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) #[[1,2]]

print(r)

r=sol.eraseOverlapIntervals([[1,2],[2,3]]) #[]

print(r)

r=sol.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]) #7

print(r)