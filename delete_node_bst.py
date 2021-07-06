class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_from_seq(seq):
    if len(seq) == 0:
        return None
    i = 0
    root = TreeNode(seq[i])
    queue = [(0, root)]
    while queue:
        tup = queue.pop(0)
        i = tup[0]
        node = tup[1]
        if len(seq) > i * 2 + 2:
            if seq[i * 2 + 1] is not None:
                node.left = TreeNode(seq[i * 2 + 1])
                queue += [(i * 2 + 1, node.left)]
            if seq[i * 2 + 2] is not None:
                node.right = TreeNode(seq[i * 2 + 2])
                queue += [(i * 2 + 2, node.right)]
    return root


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        def sub_delete(root, node, side, key):
            if node.__dict__[side].val == key:
                if node.__dict__[side].left:
                    right = node.__dict__[side].right
                    node.__dict__[side] = node.__dict__[side].left
                    node.__dict__[side].right = right
                    return root
                else:
                    node.__dict__[side] = node.__dict__[side].right
                    return root
            elif key > node.__dict__[side].val and node.__dict__[side].right:
                return sub_delete(root, node.__dict__[side], 'right', key)
            elif key < node.__dict__[side].val and node.__dict__[side].left:
                return sub_delete(root, node.__dict__[side], 'left', key)
            else:
                return root
        if root.val == key:
            if root.left:
                right = root.right
                root = root.left
                root.right = right
            else:
                root = root.right
        elif key > root.val and root.right:
            return sub_delete(root, root, 'right', key)
        elif key < root.val and root.left:
            return sub_delete(root, root, 'left', key)
        else:
            return root

if __name__ == "__main__":
    sol = Solution()
    print(sol.deleteNode(bst_from_seq([5,3,6,2,4,None,7]), 3))
    print(sol.deleteNode(bst_from_seq([5,3,6,2,4,None,7]), 0))