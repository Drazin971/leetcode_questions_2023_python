# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
      cur = dummy = ListNode()
      while list1 and list2:               
        if list1.val < list2.val:
          cur.next = list1
          list1, cur = list1.next, list1
        else:
          cur.next = list2
          list2, cur = list2.next, list2
            
      if list1 or list2:
        cur.next = list1 if list1 else list2
          
      return dummy.next
  
sol = Solution()
listnode1 = ListNode(1,ListNode(2, ListNode(4, None)))
listnode2 = ListNode(1,ListNode(3, ListNode(4, None)))

print(sol.mergeTwoLists(listnode1, listnode2).next.next.val)