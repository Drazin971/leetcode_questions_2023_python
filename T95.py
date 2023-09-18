class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:

      memo = {}  
      
      def dfs(start, end, memo):
        res = []
        if start > end:
          res.append(None)
          return res

        if (start,end) in memo:
          return memo[(start,end)]

        for i in range(start, end+1):
          lst = dfs(start, i - 1, memo)
          rst = dfs(i + 1, end, memo)


          for left in lst:
            for right in rst:
              node = TreeNode(i, left, right)
              res.append(node)
      
        memo[(start, end)] = res
        return res
      
      return  dfs(1,n,memo)
        
      

    def print_trees(self, trees: list[TreeNode]):

      if not trees: return
      
      def print_tree(tree: TreeNode):
        if not tree: 
          print("None")
          return
        print(tree.val)
        print_tree(tree.left)
        print_tree(tree.right)
        
      for tree in trees:
        print_tree(tree)


sol = Solution()
sol.print_trees(sol.generateTrees(7))


