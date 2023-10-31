class Solution:

  def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    max_level = [-float("inf")] * 10**4
    q = []
    cur_lvl = 1
    q.append((root, cur_lvl))

    if root == None: return []

    while q:
      node, level = q.pop()
      if node.left:
        q.append((node.left, level + 1))
      if node.right:
        q.append((node.right, level + 1))
      max_level[level] = max(max_level[level], node.val)
      cur_lvl = max(level, cur_lvl)

    return max_level[1:cur_lvl + 1]
