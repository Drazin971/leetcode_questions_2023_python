class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def maxLevelSum(self, root: TreeNode) -> int:
    sum_of_level=[0]*10
    current_level, max_level=0, 0
        
    def bfsearch(root: TreeNode):
      nonlocal sum_of_level, current_level, max_level
      if not root: 
        current_level -= 1
        return 
      if current_level>max_level: max_level=current_level
      sum_of_level[current_level] += root.val
      current_level += 1
      bfsearch(root.left)
      current_level += 1
      bfsearch(root.right)
      current_level -= 1
      return 
  
    bfsearch(root)

              
    return sum_of_level.index(max(sum_of_level[:max_level+1]))+1

sol=Solution()

t6=TreeNode(-10,None,None)
t5=TreeNode(-5,None,None)
t4=TreeNode(-20,None,None)
t3=TreeNode(-300,t6,None)
t2=TreeNode(-200,t4, t5)
t1=TreeNode(-100,t2,t3)

print(sol.maxLevelSum(t1)) #1

#root = [-100,-200,-300,-20,-5,-10,null] - expected 3