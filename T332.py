class Solution:
  def findItinerary(self, tickets: list[list[str]]) -> list[str]:
    for ticket in tickets:
      start, end = ticket
      print(start, end)

sol = Solution() 

print(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]) #["JFK","ATL","JFK","SFO","ATL","SFO"]




