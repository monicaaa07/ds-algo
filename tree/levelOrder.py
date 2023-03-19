# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def traverseTree(root,level):
            nonlocal result
            if root is None:
                return 

            if len(result) > level:
                result[level].append(root.val)
            else:
                result.append([root.val])

            traverseTree(root.left,level + 1) 
            traverseTree (root.right, level +1)

            return

        traverseTree(root, 0)
        return result
        
