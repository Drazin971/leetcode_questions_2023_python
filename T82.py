class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
     
class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    start = ListNode()
    start.next = head
    prev = head
    while head and head.next:
      if head.val == head.next.val:
        while head and head.next and head.val == head.next.val:
          head = head.next
      else:
        if prev == start.next:
          start.next=head.next
        prev.next = head.next
        
      head = head.next

    return start.next
    
    

l15=ListNode(5,None)
l14=ListNode(3,l15)
l13=ListNode(3,l14)
l12=ListNode(1,l13)
l11=ListNode(1,l12)


sol=Solution()

sol.deleteDuplicates(l11)

while l11:
  print(l11.val) 
  l11=l11.next













 



