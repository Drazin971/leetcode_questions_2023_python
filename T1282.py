from collections import defaultdict

class Solution:
  def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
    groups = defaultdict(int)

    for i in range(len(groupSizes)):
      groups[groupSizes[i]].add(i)

    print groups

sol = Solution()

print(sol.groupThePeople(groupSizes = [3,3,3,3,3,1,3])) #[[5],[0,1,2],[3,4,6]]

print(sol.groupThePeople(groupSizes = [2,1,3,3,3,2])) #[[1],[0,5],[2,3,4]]