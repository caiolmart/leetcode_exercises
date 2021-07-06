class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_from_list(l):
    head = ListNode(l[0])
    node = head
    for val in l[1:]:
        node.next = ListNode(val)
        node = node.next
    return head


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pointer1, pointer2 = head, head
        for _ in range(n):
            pointer2 = pointer2.next
        if pointer2 is None:
            pointer1 = pointer1.next
            return pointer1
        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        if pointer1.next is not None:
            pointer1.next = pointer1.next.next
        else:
            del pointer1
        return head

if __name__ == "__main__":
    sol = Solution()
    
    head = create_from_list([1,2,3,4,5])
    print(sol.removeNthFromEnd(head, 1))
