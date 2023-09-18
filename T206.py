class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution:
  def reverseList(self, head: ListNode) -> ListNode:

    if not head: return None

    ll = []

    while head:
      ll.append(head)
      head=head.next

    for i in range(len(ll)-1,0,-1):
      ll[i].next=ll[i-1]

    ll[0].next = None 

    return ll[len(ll)-1]
