class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
      if root:
        branch_left = root.left
        branch_right = root.right
      return self.checkBranch(branch_left, branch_right)
    
    def checkBranch(self, left: TreeNode, right: TreeNode) -> bool:
          if left and right:
            return left.val==right.val and self.checkBranch(left.left, right.right) and self.checkBranch(left.right, right.left)
          return left is right
        
      

sol = Solution()

l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(2)
l4 = TreeNode(3)
l5= TreeNode(4)
l6 = TreeNode(3)
l7= TreeNode(4)

l1.left = l2
l1.right = l3