class Solution:
  def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

      temp = head
      total_nodes = 0
      sol = []

      while temp:
          temp = temp.next
          total_nodes += 1
      
      rest_value = total_count % k
      whole_volue = total_count // k
      
      temp = head.copy

      return sol