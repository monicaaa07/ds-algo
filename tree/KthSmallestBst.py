# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        uk = 0
        result = 0
        def inorder(root,k):
            if  not root:
                return False
            left =  inorder(root.left,k)
            nonlocal uk
            nonlocal result
            uk = uk + 1
            if left:
                return left
            if uk == k:
                result = root.val
                return True
            else:
                return inorder(root.right,k)
        inorder(root,k)
        return result



