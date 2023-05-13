# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag=False
        
        def dfs(root):
            
            if not root:
                return -1
            left=1+dfs(root.left)
            right=1+dfs(root.right)
            
            if abs(right-left)>1:
                nonlocal flag
                flag=True
            
            return max(left,right)
        
        n=dfs(root)
        if flag:
            return False
        else:
            return True
        
            
            