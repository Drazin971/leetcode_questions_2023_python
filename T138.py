class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random
     
class Solution:
  def copyRandomList(self, head: [Node]) -> [Node]:
    list_of_nodes = []
    new_nodes = []
    if not head:
      return None
    while head:
      new_node = Node(head.val)
      list_of_nodes.append(head) 
      new_nodes.append(new_node)
      head = head.next
    
    for node in list_of_nodes:
      if node.next!=None:
       new_nodes[list_of_nodes.index(node)].next = new_nodes[list_of_nodes.index(node.next)]
      if node.random!=None:
       new_nodes[list_of_nodes.index(node)].random = new_nodes[list_of_nodes.index(node.random)]

    return new_nodes[0]

l15=Node(1,None,None)
l14=Node(10,l15,None)
l13=Node(19,l14,None)
l12=Node(13,l13,None)
l11=Node(9,l12,None)
l12.random=l11
l13.random=l15
l14.random=l13
l15.random=l11


sol=Solution()

print(sol.copyRandomList(l11)) 
#print(sol.copyRandomList([l11,l12,l13,l14,l15]).next.val) 
#print(sol.copyRandomList([l11,l12,l13,l14,l15]).next.next.val) 
#print(sol.copyRandomList([l11,l12,l13,l14,l15]).next.next.next.val) 






 



