class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def allPossibleFBT(self, n: int) -> list[TreeNode]:
    if n%2 == 0: return []

    dp ={0:[], 1:[TreeNode()]}
    
    def make_nodes(n: int):
      if n in dp:
        return dp[n]

      res = []

      for l in range(n):
        left = make_nodes(l) 
        right = make_nodes(n-1-l)

        for t1 in left:
          for t2 in right:
            res.append(TreeNode(0,t1,t2))

      dp[n] = res
      return res
      
    return make_nodes(n)
      

sol = Solution()

def print_Tree(root: TreeNode):
  if not root: 
    print(root.val)
    return
  print(root.val)
  print_Tree(root.left)
  print_Tree(root.right)

r=sol.allPossibleFBT(n = 7) #Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

for root in r:
  print_Tree(root)

r=sol.allPossibleFBT(n = 2) #Output: []

for root in r:
  print_Tree(root)