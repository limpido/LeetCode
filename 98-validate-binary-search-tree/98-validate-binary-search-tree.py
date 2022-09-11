# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_BST(cur, min_val, max_val):
            if not cur:
                return True
            if cur.val < min_val or cur.val > max_val:
                return False
            return check_BST(cur.left, min_val, cur.val-1) and check_BST(cur.right, cur.val+1, max_val)
        
        return check_BST(root, float(-inf), float(inf))