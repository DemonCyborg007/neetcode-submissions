# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(r1,r2):
            if not r1 and not r2: 
                # print(r1.val,r2.val)
                return True
            if r1 and r2 and r1.val==r2.val:
                print("sametree",r1.val,r2.val)
                ls=sameTree(r1.left,r2.left) 
                rs=sameTree(r1.right,r2.right)
                print(ls)
                print(rs)
                return ls and rs
                # return sameTree(r1.left,r2.left) and sameTree(r1.right,r2.right)
            else:
                return False
        # def sameTree(r1, r2):
            # if not r1 and not r2: 
            #     return True
            # if r1 and r2 and r1.val == r2.val:
            #     return sameTree(r1.left, r2.left) and sameTree(r1.right, r2.right)
            # else:
            #     return False
        def findsubrootinroot(root,sub):
            if root and sub and root.val == sub.val:
                print(root.val,sub.val)
                subans = sameTree(root,sub)
                print("subans",subans)
                if subans == True:
                    return True
                # return sameTree(root,sub)
            lans,rans=False,False
            if root.left: 
                lans=findsubrootinroot(root.left,sub)
            if root.right: 
                rans=findsubrootinroot(root.right,sub)
            print("ok",lans,rans)
            return lans or rans
        ans=findsubrootinroot(root,subRoot)
        print("final",ans)
        return ans
        