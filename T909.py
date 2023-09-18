from collections import deque

class Solution:
  def snakesAndLadders(self, board: list[list[int]]) -> int:
    start = 1
    goal = len(board)**2
    visited = set()
    q=deque()
    q.append([start,0])
    board.reverse()

    def int_to_pos(square) -> list:
      r = (square-1) // len(board)
      c = (square-1) % len(board)
      if r % 2:
        c=len(board)-1-c
        
      return [r,c]

    while q:
      square, moves = q.popleft()
      for roll in range(1,7):
        nsquare=square+roll
        r,c = int_to_pos(nsquare)
        if board[r][c] != -1:
          nsquare = board[r][c]
        if nsquare == goal:
          return moves+1
        if nsquare not in visited:
          visited.add(nsquare)
          q.append([nsquare,moves+1])
    return -1
        
      
                     
sol = Solution()

r=sol.snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]) #4

print(r)

r=sol.snakesAndLadders(board = [[-1,-1],[-1,3]]) #1

print(r)