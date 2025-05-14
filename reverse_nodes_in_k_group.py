from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.value_list)
    
    @property
    def value_list(self):
        value_list = [self.val]
        node = self
        while node.next:
            node = node.next
            value_list.append(node.val)
        return value_list

    
    @classmethod
    def from_list(cls, value_list):
        root = cls(value_list[0])
        node = root
        for val in value_list[1:]:
            node.next = cls(val)
            node = node.next
        return root

"""
A -> B -> C

tail = A
previous = tail = A
current = tail.next = B
next = current.next = C
current.next = previous = A
previous = current
current = next

"""


class Solution:
    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        """
        store current node as tail of the group `group_tail`
        current_node = head
        for _ in range(k - 1) # except the head of the node
            next_node = current_node.next
            reverse the next of every node
        
        the current node is now the root
        the group_tail now has no meaningful next
        set group_tail next and a recursive call to the next node
        """
        current_node = head
        for _ in range(k-1):
            if not current_node.next:
                return head
            current_node = current_node.next

        group_tail = head
        previous_node = group_tail
        current_node = group_tail.next
        for _ in range(k - 1):
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        if not current_node:
            group_tail.next = None
            return previous_node
        
        group_tail.next = self.reverseKGroup(current_node, k)
        return previous_node




case_1 = [1,2,3,4,5]
root = ListNode.from_list(case_1)
sol = Solution()
res = sol.reverseKGroup(root, 3)
print(res)
