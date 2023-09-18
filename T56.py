class Solution:
  def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    intervals = sorted(intervals)
    #print(intervals)

    merged = []

    for interval in intervals:
      if not merged or interval[0]>merged[-1][1]:
        merged.append(interval)
      else:
        merged[-1][1]=max(merged[-1][1],interval[1])
    return merged

sol=Solution()

print(sol.merge(intervals = [[1,3],[0,6],[8,10],[15,18]])) #[[1,6],[8,10],[15,18]]

print(sol.merge(intervals = [[1,4],[4,5]])) #[[1,5]]