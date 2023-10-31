class Solution:
  def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
    st = []
    for i in range(len(mat)):
      st.append((sum(mat[i]),i))
 
    st.sort()

    return [t[1] for t in st[:k]]
    
    

sol = Solution()

print(sol.kWeakestRows(
 [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],k=3))
