# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, value_list):
        if len(value_list) == 0:
            return None

        root = cls(value_list[0])
        if len(value_list) == 1:
            return root

        node = root
        for next_node in value_list[1:]:
            node.next = cls(next_node)
            node = node.next

        return root

    def __repr__(self):
        this_str = f"{self.val}"
        node = self
        while node.next:
            node = node.next
            this_str += f" {node.val}"
        return this_str


class Solution:
    def _heapify(self, heap, idx):
        left = idx * 2 + 1
        right = idx * 2 + 2
        smallest = idx
        if left < len(heap) and heap[left].val < heap[smallest].val:
            smallest = left
        if right < len(heap) and heap[right].val < heap[smallest].val:
            smallest = right
        if smallest != idx:
            aux = heap[idx]
            heap[idx] = heap[smallest]
            heap[smallest] = aux
            self._heapify(heap, smallest)

    def _build_heap(self, heap):
        for idx in range(len(heap) // 2 - 1, -1, -1):
            self._heapify(heap, idx)

    def _get_next_node_and_update(self, heap):
        next_node = heap[0]
        if next_node.next:
            heap[0] = next_node.next
            self._heapify(heap, 0)
            next_node.next = None
        else:
            heap[0] = heap[-1]
            del heap[-1]
            self._heapify(heap, 0)

        return next_node

    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        """
        - Create a (min) heap with the values of every first element of
        the lists.
        - Create a sorted linked list `output`
        - While there are elements in the lists:
          - Take the root of the heap and put into a new linked list
          - Take the next value of list or the last value of the heap and put on
            top and heapify.
        """

        # build heap of lists and create the output linked list
        heap = [l for l in lists if l is not None]
        if not heap:
            return None
        self._build_heap(heap)

        root = self._get_next_node_and_update(heap)
        cur_node = root
        # loop while there are elements in lists
        while heap:
            next_node = self._get_next_node_and_update(heap)
            cur_node.next = next_node
            cur_node = next_node
        return root


def create_input(lists):
    roots = []
    for this_list in lists:
        root = ListNode.from_list(this_list)
        roots.append(root)
    return roots


case_1 = [[2, 6], [1, 3, 4], [1, 4, 5]]
sol = Solution()
output = sol.mergeKLists(create_input(case_1))
print(output)
case_2 = [[]]
output = sol.mergeKLists(create_input(case_2))
print(output)
case_3 = []
output = sol.mergeKLists(create_input(case_3))
print(output)
case_4 = [[1, 2, 3, 4, 5, 6], []]
output = sol.mergeKLists(create_input(case_4))
print(output)
