class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
     
class Solution:
  def rotateRight(self, head: ListNode, k: int) -> ListNode:
    heads = []
    
    if head==None: return head

    while head:
      heads.append(head)
      head=head.next

    if len(heads)<2: return heads[0]

    heads[len(heads)-1].next = heads[0]

    k=k % len(heads)
    
    for _ in range(k):
      temp=heads.pop()
      heads.insert(0,temp)
    
    heads[len(heads)-1].next = None
  
    return heads[0] if heads else None
    
    

l15=ListNode(5,None)
l14=ListNode(4,l15)
l13=ListNode(3,l14)
l12=ListNode(3,l13)
l11=ListNode(1,l12)


sol=Solution()

newNode = sol.rotateRight(l11,8)

while newNode:
  print(newNode.val) 
  newNode=newNode.next










 



