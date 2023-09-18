class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    head = curr_node = ListNode()
  
    while l1 or l2 or carry!=0:
      val_l1 = l1.val if l1 else 0
      val_l2 = l2.val if l2 else 0
      
      if val_l1+val_l2+carry>=10:
        node_value = val_l1+val_l2+carry-10
        carry = 1
      else:
        node_value = val_l1+val_l2+carry
        carry=0

      next_node = ListNode(node_value)
      curr_node.next = next_node
      curr_node  = next_node

      l1=l1.next if l1 else None
      l2=l2.next if l2 else None

    result = head.next
    head.next=None
    return result