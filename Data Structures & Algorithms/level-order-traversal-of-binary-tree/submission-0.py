# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d={}
        height=0
        def dfs(height,root):
            if root == None:
                return 0
            if height in d:
                val = d[height]
                val.append(root.val)
                d[height] = val
            else:
                d[height]=[root.val]
            lst = dfs(height+1,root.left)
            rst = dfs(height+1,root.right)
            return 0
        dfs(height,root)
        ans=[]
        for k,v in d.items():
            ans.append(v)
        return ans
        