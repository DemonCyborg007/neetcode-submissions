# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recur(root,res):
            if root is None:
                return 0
            lst = recur(root.left,res)
            rst = recur(root.right,res)
            res[0] = max(res[0],lst+rst)
            return max(lst,rst)+1
        res = [0]
        recur(root,res)
        return res[0]
        