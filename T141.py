class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    while head:
      if head.next==None:
        return False
      if head.val != 10**6:
        head.val = 10**6
        head = head.next
      else:
        return True