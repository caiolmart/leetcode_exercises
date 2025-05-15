from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _get_max_descending_sum(self, node):
        if hasattr(node, "max_descending_sum"):
            return node.max_descending_sum

        max_descending_sum = node.val
        if node.left:
            max_descending_sum = max(
                max_descending_sum,
                node.val + self._get_max_descending_sum(node.left),
            )
        if node.right:
            max_descending_sum = max(
                max_descending_sum,
                node.val + self._get_max_descending_sum(node.right),
            )
        node.max_descending_sum = max_descending_sum
        return max_descending_sum

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Three options:
        max_path_sum includes root and has a sum to the left and to the right
        max_path_sum is only on the left self.maxPathSum(root.left)
        max_path_sum is only on the right self.maxPathSum(root.right)

        if it includes root, we must find the max sum of a path that ends with left, and another that ends with right.

        We can store for each node, the maximum value of the path that ends
        on them. The path between it and its children.

        Then the max path sum is either:
            - max(root.left.max_descending_sum, 0) + max(root.right.max_descending_sum, 0) + root.val
            - self.maxPathSum(root.left)
            - self.maxPathSum(root.right)
        """

        left_max_descending_sum = 0
        if root.left:
            left_max_descending_sum = self._get_max_descending_sum(root.left)
        right_max_descending_sum = 0
        if root.right:
            right_max_descending_sum = self._get_max_descending_sum(root.right)
        include_root = (
            max(left_max_descending_sum, 0)
            + max(right_max_descending_sum, 0)
            + root.val
        )
        ans = include_root
        if root.left:
            ans = max(ans, self.maxPathSum(root.left))
        if root.right:
            ans = max(ans, self.maxPathSum(root.right))
        return ans
