class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
     if not root: return 0
     if root.left==None and root.right==None:
       return 1
       
     return min(self.minDepth(root.left) if root.left else float('inf'), self.minDepth(root.right) if root.right else float('inf')) +1
    
           
      

sol = Solution()

l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(2)
l4 = TreeNode(1)


l1.left = l2
l1.right = l3
l3.left = l4
 
print(sol.minDepth(l1))













 



