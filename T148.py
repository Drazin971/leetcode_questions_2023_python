class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution:
  def sortList(self, head: ListNode) ->ListNode:

    def m_list(head: ListNode):
      ans = []
      while head:
        ans.append(head)
        head=head.next
      return ans

    if not head:return None
    
    ans = m_list(head)

    ans.sort(key=lambda x: x.val)

    for i in range(len(ans)-1):
      ans[i].next=ans[i+1]

    ans[len(ans)-1].next=None
    
    return ans[0]

sol=Solution()

def make_list(head: list):
  start = ListNode(head[0])
  prev = start
  for i in range(1,len(head)):
    next = ListNode(head[i])
    prev.next=next
    prev = next

  return start

def print_list(head: ListNode):
  while head:
    print(head.val)
    head=head.next
  return

l = make_list(head = [-1,5,3,4,0])

print_list(l)

r=sol.sortList(l)

print_list(r)