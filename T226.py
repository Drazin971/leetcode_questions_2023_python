class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
     
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
      if root==None:
        return None
        
      dummy=root.left
      root.left=root.right
      root.right=dummy

      self.invertTree(root.left)
      self.invertTree(root.right)
      
      return root
    

l15=TreeNode(1,None,None)
l14=TreeNode(3,None,None)
l13=TreeNode(2,l15,l14)


sol=Solution()

print(sol.invertTree(l13).val) 
print(sol.invertTree(l13).left.val) 
print(sol.invertTree(l13).right.val) 







 



