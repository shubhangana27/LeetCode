# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = ""
        current = l1
        while current:
            l1_str = str(current.val) + l1_str  # Reverse order
            current = current.next
        
        # Convert l2 to string (digits in reverse order as stored)
        l2_str = ""
        current = l2
        while current:
            l2_str = str(current.val) + l2_str  # Reverse order
            current = current.next
        
        # Convert strings to integers, add them
        num1 = int(l1_str) if l1_str else 0
        num2 = int(l2_str) if l2_str else 0
        total = num1 + num2
        
        # Convert total back to linked list
        if total == 0:
            return ListNode(0)
        
        # Create result linked list in reverse order
        total_str = str(total)
        temp = ListNode(0)
        current = temp
        
        # Iterate through string in reverse
        for digit in reversed(total_str):
            current.next = ListNode(int(digit))
            current = current.next
        
        return temp.next