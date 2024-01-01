class Solution:
  def findMode(self, root: Optional[TreeNode]) -> List[int]:
      res = defaultdict(int)
      q = []

      q.append(root)

      while q:
          node = q.pop(0)
          if node:
              res[node.val] += 1
              q.append(node.left)
              q.append(node.right)
      print(res)

      mnode = max(res.values())

      return [k for k, v in res.items() if v == mnode]