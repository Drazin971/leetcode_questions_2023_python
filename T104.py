class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
         
    def maxDepth(self, root: TreeNode) -> int:  
        return self.checkDepth(root,0)

    def checkDepth(self, root: TreeNode, depth: int) -> int:
       if not root:
         return depth
       else:
         return (max(self.checkDepth(root.left, depth+1), self.checkDepth(root.right, depth+1))) 
        

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

l2.left= l4
l2.right=l5

l3.left=l7
l3.right = l6


print(sol.maxDepth(l1))