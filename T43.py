class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution:
  def mergeKLists(self, lists: list[[ListNode]]) -> ListNode:

    def m_list(head: ListNode):
      ans = []
      while head:
        ans.append(head)
        head=head.next
      return ans

    if not lists: return None

    ans = []
    for item in lists:
        n = m_list(item)
        for node in n:
          ans.append(node)

    ans.sort(key=lambda x: x.val)

    for i in range(len(ans)-1):
      ans[i].next=ans[i+1]

    if len(ans)>0:
      ans[len(ans)-1].next=None
      return ans[0]
    else:
      return None

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

l1 = make_list(head = [-1,5,3,4,0])
l2 = make_list(head = [1,4,5])
l3 = make_list(head = [2,6])

r=sol.mergeKLists([[l1],[l2],[l3]])

print_list(r)