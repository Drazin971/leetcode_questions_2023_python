class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def getMinimumDifference(self, root: TreeNode) -> int:
    values=[]
    min_difference = float('inf')
    
    def bfsearch(root: TreeNode):
      nonlocal values
      if not root: return 
      bfsearch(root.left)
      values.append(root.val)
      bfsearch(root.right)
      return 
  
    bfsearch(root)
    for i in range(len(values)):
      min_difference = min(abs(values[i]-values[i-1]), min_difference)
            
    return min_difference

sol=Solution()

t5=TreeNode(49,None,None)
t4=TreeNode(12,None,None)
t3=TreeNode(48,t4,t5)
t2=TreeNode(0,None, None)
t1=TreeNode(1,t2,t3)

print(sol.getMinimumDifference(t1)) #1