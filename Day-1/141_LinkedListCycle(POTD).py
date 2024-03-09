class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while True:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
