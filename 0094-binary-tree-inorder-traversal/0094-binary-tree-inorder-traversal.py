# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        def travel(root):
            if not root:
                return
            if root.left:
                travel(root.left)
            a.append(root.val)
            if root.right:
                travel(root.right)
        travel(root)
        return a
            
        
        