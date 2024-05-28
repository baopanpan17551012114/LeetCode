# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_min_value(self, root):
        if root is None:
            return 2 ** 31 - 1
        if root.left is None and root.right is None:
            return root.val
        return min(root.val, self.get_min_value(root.left), self.get_min_value(root.right))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        left_min = self.get_min_value(root.left)
        right_min = self.get_min_value(root.right)
        return (left_min < root.val < right_min) and self.isValidBST(root.left) and self.isValidBST(root.right)


if __name__ == '__main__':
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l2.right = l3
    res = Solution().isValidBST(l2)
    print(res)