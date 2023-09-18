class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
     
class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    heads = []
    while head:
      heads.append(head)
      head=head.next

    
    last = len(heads)

    print(last-n-1,last-n+1)
    
    if last==1:
      heads[0]=None
    else:
      if last==n:
        return heads[1]
      heads[last-n-1].next = heads[last-n+1] if n>1 else None

    return heads[0]
    
    

l15=ListNode(5,None)
l14=ListNode(4,l15)
l13=ListNode(3,l14)
l12=ListNode(2,l13)
l11=ListNode(1,l12)

l2=ListNode(2,None)
l1=ListNode(1,l2)

sol=Solution()

print(sol.removeNthFromEnd(l11,2).val) 
print(l11.next.val) 
print(l11.next.next.val) 
print(l11.next.next.next.val) 

print(sol.removeNthFromEnd(l1,2).val) 












 



