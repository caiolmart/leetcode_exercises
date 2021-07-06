class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.aux_is_valid(root)
        
    def aux_is_valid(self, root, min_val=None, max_val=None) -> bool:
        if not root:
            return True
        if min_val is not None and root.val <= min_val:
            return False
        if max_val is not None and root.val >= max_val:
            return False
        if not self.aux_is_valid(root.left, min_val, root.val):
            return False
        if not self.aux_is_valid(root.right, root.val, max_val):
            return False
        return True