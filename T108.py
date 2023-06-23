class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
       start=0
       end=len(nums)-1
       return self.helperSortedArrayToBST(nums, start, end)

    def helperSortedArrayToBST(self, nums: list[int], start, end) -> TreeNode:
      if start > end:
        return None
      mid = (start+end)//2
      root = TreeNode(nums[mid])
      root.left = self.helperSortedArrayToBST(nums, start, mid-1)
      root.right = self.helperSortedArrayToBST(nums, mid+1, end)
      return root
        

sol = Solution()


print(sol.sortedArrayToBST([-10,-3,0,5,9]).left.val)
