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
    def rob(self, root: Optional[TreeNode]) -> int:
        if hasattr(root, "with_root_total"):
            return max(root.with_root_total, root.no_root_total)

        root.with_root_total = root.val or 0
        root.no_root_total = 0
        if root.left:
            root.no_root_total += self.rob(root.left)
            root.with_root_total += root.left.no_root_total
        if root.right:
            root.no_root_total += self.rob(root.right)
            root.with_root_total += root.right.no_root_total

        return max(root.with_root_total, root.no_root_total)


sol = Solution()
root = TreeNode.from_list([3, 2, 3])
print(sol.rob(root))
root = TreeNode.from_list([3, 2, 3, None, 3, None, 1])
print(sol.rob(root))
root = TreeNode.from_list([4, 1, None, 2, None, 3]) # should be 7
print(sol.rob(root))