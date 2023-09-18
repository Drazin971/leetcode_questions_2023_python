
import collections

class Solution:
  def exist(self, board: list[list[str]], word: str) -> bool:

    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    visited = set()
    found=False

    def check_board_is_legal():
      boardDic = defaultdict(int)
      for i in range(len(board)):
        for j in range(len(board[0])):
          boardDic[board[i][j]] += 1

      wordDic = counter(word)
      for c in wordDic:
        if c not in boardDic or boardDic[c] < wordDic[c]:
    	     return False

    def check_solution(row: int, column: int, idx: int):

      nonlocal found

      def is_valid(row: int, column: int):
        return False if row < 0 or row > len(board)-1 or column < 0 or column > len(board[0])-1 else True
      
      if idx == len(word):
        found=True
        return 

      visited.add((row,column))
      
      for direction in directions:
         delta_row, delta_colum = direction
         r, c = row + delta_row, column + delta_colum
         if is_valid(r,c) and board[r][c]==word[idx] and (r,c) not in visited:
           check_solution(r,c,idx+1)
          
      visited.remove((row,column))

    if not check_board_is_legal: return False
    
    for r in range(len(board)):
      for c in range(len(board[0])):
        if board[r][c]==word[0]:
          check_solution(r,c,1)
        if found:
          return True

    return False

sol = Solution()

r=sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB") #false

print(r)

r=sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED") #true

print(r)

r=sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE") #true

print(r)

r=sol.exist(board = [["a","b"]], word = "ba") #true

print(r)

r=sol.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]], word =
"AAAAAAAAAAAAABB") #false

print(r)