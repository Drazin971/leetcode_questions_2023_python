class Solution:
  def generateParenthesis(self, n: int) -> list[str]:
    sol = []
    op="("
    cl=")"

    def search(open_count: int, close_count: int, curr: str):
      if open_count>n or close_count>n:
        return
      if open_count==close_count and len(curr)==n*2:
        sol.append(curr)
        return

      curr+=op
      search(open_count+1,close_count,curr)
      curr=curr[:-1]
      if close_count<open_count:
        curr+=cl
        search(open_count,close_count+1,curr)
        curr=curr[:-1]
      
    search(0,0,"")

    return sol

sol = Solution()

r=sol.generateParenthesis(3) #["((()))","(()())","(())()","()(())","()()()"]

print(r)

r=sol.generateParenthesis(1) #["()"]

print(r)

