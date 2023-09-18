import heapq

class Solution:
  def minimumEffortPath(self, heights: list[list[int]]) -> int:

    path = []

    rows = len(heights)
    columns = len(heights[0])
    
    def find_neighbours(node):
      neighbours = []
      directions = [(-1,0), (0, -1), (1,0), (0,1)]
      x, y = node

      for direction in directions:
        dx, dy = direction
        nx, ny = x + dx, y + dy
        if nx>=0 and ny>=0 and ny<columns and nx<rows: 
          neighbours.append((nx, ny))
             
      return neighbours

    effort_path = [[float('inf') for _ in range(columns)]  for _ in range(rows)]
    effort_path[0][0] = 0

    path.append((0,0))
    while path:     
      #print(effort_path)
      current_node = heapq.heappop(path)
      neighbours = find_neighbours(current_node)
      for neighbour in neighbours:
          x, y = neighbour
          new_effort = max(effort_path[current_node[0]][current_node[1]],abs(heights[x][y] - heights[current_node[0]][current_node[1]]))
          if new_effort < effort_path[x][y]:
            effort_path[x][y] = new_effort
            heapq.heappush(path, neighbour)
            
        
    return effort_path[rows-1][columns-1]

sol = Solution()

print(sol.minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]])) #2

print(sol.minimumEffortPath(heights = [[1,10,6,7,9,10,4,9]])) #9

print(sol.minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]])) #1


