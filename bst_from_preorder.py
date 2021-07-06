from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(val=preorder[0])
        if len(preorder) == 1:
            return root
        elif len(preorder) == 2:
            if preorder[1] < root.val:
                root.left = TreeNode(val=preorder[1])
            else:
                root.right = TreeNode(val=preorder[1])
            return root

        idx = len(preorder) // 2
        max_idx = len(preorder) - 1
        min_idx = 1
        while idx < len(preorder) - 1 and idx >= 1 and (preorder[idx] > root.val or root.val > preorder[idx + 1]):
            if preorder[idx] > root.val:
                max_idx = idx - 1
                idx = min_idx + (max_idx - min_idx) // 2
            else:
                min_idx = idx + 1
                idx = min_idx + (max_idx - min_idx) // 2
        
        left_list = preorder[1:(idx + 1)]
        right_list = preorder[(idx + 1):]
        
        root.left = self.bstFromPreorder(left_list)
        root.right = self.bstFromPreorder(right_list)
        return root
            
if __name__ == "__main__":
    sol = Solution()
    #print(sol.bstFromPreorder([8,5,1,7,10,12]))
    #print(sol.bstFromPreorder([4,2]))
    #print(sol.bstFromPreorder([19,4,13,7,20]))
    #print(sol.bstFromPreorder([6,3,4,5,8,12,18,13]))
    print(sol.bstFromPreorder([4,5,14,20])) 