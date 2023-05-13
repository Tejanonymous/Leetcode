# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxi=0
        
        
        def height(root):
            
            if not root:
                return -1
            
            left=1+height(root.left)
            right=1+height(root.right)
            nonlocal maxi
            
            maxi=max(maxi,left+right)
            
            return max(left,right)
        x=height(root)    
        return maxi
        
    