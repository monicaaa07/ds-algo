# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodesHelper(root, max_so_far):
            if root is None:
                return 0
           
            left = goodNodesHelper(root.left,max(root.val,max_so_far))
            right = goodNodesHelper(root.right,max(root.val,max_so_far))

            if root.val >= max_so_far:
                return left +right+1
            else:
                return left + right
        return goodNodesHelper(root,root.val)

