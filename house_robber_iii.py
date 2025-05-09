# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, tree_list):
        tree_root = cls(val=tree_list[0])
        queue = [tree_root]
        i = 1
        while i < len(tree_list):
            curr = queue.pop(0)
            if tree_list[i] is not None:
                curr.left = cls(val=tree_list[i])
                queue.append(curr.left)
            i += 1
            if i < len(tree_list):
                if tree_list[i] is not None:
                    curr.right = cls(tree_list[i])
                    queue.append(curr.right)
                i += 1
        return tree_root


class Solution:
    def _get_totals(self, node, depth):
        with_root_total = 0
        no_root_total = 0
        if depth % 2:
            no_root_total += node.val or 0
            if node.left:
                w, n = self._get_totals(node.left, depth + 1)
                with_root_total += w
                no_root_total += n
            if node.right:
                w, n = self._get_totals(node.right, depth + 1)
                with_root_total += w
                no_root_total += n
        else:
            with_root_total += node.val or 0
            if node.left:
                w, n = self._get_totals(node.left, depth + 1)
                with_root_total += w
                no_root_total += n
            if node.right:
                w, n = self._get_totals(node.right, depth + 1)
                with_root_total += w
                no_root_total += n
        return (with_root_total, no_root_total)

    def rob(self, root: Optional[TreeNode]) -> int:
        with_root_total, no_root_total = self._get_totals(root, 0)
        return max(with_root_total, no_root_total)


sol = Solution()
root = TreeNode.from_list([3, 2, 3, None, 3, None, 1])
print(sol.rob(root))
root = TreeNode.from_list([4, 1, None, 2, None, 3]) # should be 7
print(sol.rob(root))