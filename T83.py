class Solution:
    def deleteDuplicates(self, head: Node) -> Node:
      pointer = head
      while (pointer and pointer.next):
        if pointer.data == pointer.next.data:
          pointer.next = pointer.next.next
          continue
        pointer = pointer.next
          
      
        
      return head

# Example usage:
arr = [1,1,2,3,3]
head = createLinkedList(arr)

sol = Solution()

print(sol.deleteDuplicates(head).next.next.data)

