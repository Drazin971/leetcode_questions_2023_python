class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    pass
    
    def create_list(num: ListNode):
      s=""
      while num:
        s=s+str(num.val)
        num=num.next
      return s

    def create_nodes(l: list) -> ListNode:
      root = prev = ListNode(-1)
      root.next=prev
      for item in l:
        node = ListNode(item)
        prev.next=node
        prev=node
      return root.next

    sum_of_lists = "" 
    sum_of_lists += create_list(l1) + "+" +create_list(l2)

    return create_nodes(str(eval(sum_of_lists)))

def create_nodes(l: list) -> ListNode:
  root = prev = ListNode(-1)
  root.next=prev
  for item in l:
    node = ListNode(item)
    prev.next=node
    prev=node
  return root.next

def print_num(num: ListNode):
  while num:
    print(num.val)
    num=num.next

l1 = [7,2,4,3]
l2 = [5,6,4]

num1 = create_nodes(l1)
num2 = create_nodes(l2)

sol=Solution()
print_num(sol.addTwoNumbers(num1,num2))


