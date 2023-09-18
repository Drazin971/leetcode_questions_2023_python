class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
     
class Solution:
  def partition(self, head: ListNode, x: int) -> ListNode:
    heads_less = []
    heads_more = []
    
    if head==None: return head

    while head:
      heads_less.append(head) if head.val<x else heads_more.append(head)
      head=head.next

    if heads_less:
      for i in range(len(heads_less)-1):
        if heads_less[i+1]:
          heads_less[i].next=heads_less[i+1] 
      heads_less[len(heads_less)-1].next=heads_more[0] if heads_more else None
        
    if heads_more:
      for i in range(len(heads_more)-1):
        heads_more[i].next=heads_more[i+1]
      heads_more[len(heads_more)-1].next = None

    return heads_less[0] if heads_less else heads_more[0]   
    

l15=ListNode(6,None)
l14=ListNode(5,l15)
l13=ListNode(3,l14)
l12=ListNode(1,None)
l11=ListNode(2,l12)


sol=Solution()

newNode = sol.partition(l11,2)

while newNode:
  print(newNode.val) 
  newNode=newNode.next










 














 



