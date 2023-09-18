class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
     
class Solution:
  def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    if left==right:
      return head
    start = head
    list_of_nodes=[]
    while right>=1:
      if left<=2:
        list_of_nodes.append(head)
      head = head.next
      left-=1
      right-=1

    items_to_reverse=len(list_of_nodes)

    if items_to_reverse==2:
      start=list_of_nodes[1]
      list_of_nodes[1].next=list_of_nodes[0]
      list_of_nodes[0].next=list_of_nodes[1]

    list_of_nodes[0].next=list_of_nodes[items_to_reverse-1]
    list_of_nodes[1].next=list_of_nodes[items_to_reverse-1].next
   
    for i in range(items_to_reverse-1,1,-1):
      #print(i, items_to_reverse-i-1)
      list_of_nodes[i].next=list_of_nodes[i-1]
      
    return start
    

l15=ListNode(5,None)
l14=ListNode(4,l15)
l13=ListNode(3,l14)
l12=ListNode(5,l13)
l11=ListNode(3,l12)

sol=Solution()

print(sol.reverseBetween(l11,1,2).val) 
print(sol.reverseBetween(l11,1,2).next.val) 






 



