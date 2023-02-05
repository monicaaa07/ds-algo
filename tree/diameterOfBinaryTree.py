# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/diameter-of-binary-tree/description/
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
         diameter = 0

         def diameterOfBinaryTreeHelper(root: Optional[TreeNode]) -> int:
            nonlocal diameter 
            
            if root is None:
                return 0 
            else:
                hll = diameterOfBinaryTreeHelper(root.left)
                hlr = diameterOfBinaryTreeHelper(root.right)
                diameter  = max(max_pl ,hll + hlr)
                return  max(hll, hlr) + 1

         diameterOfBinaryTreeHelper(root)
         return(diameter)
