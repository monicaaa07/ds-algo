# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        
        def lowestCommonAncestorHelper(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
            nonlocal lca
            if root is None :
                return False

            leftVal =  lowestCommonAncestorHelper(root.left, p, q) 
            rightVal=lowestCommonAncestorHelper(root.right, p, q) 

            mid = root == p or root == q

            if mid + leftVal + rightVal >= 2:
                lca = root

            return mid or leftVal or rightVal


#           MY Version
            # if root.val == p.val or root.val == q.val :
            #     print("true")
            #     if lowestCommonAncestorHelper(root.left, p, q) or lowestCommonAncestorHelper(root.right, p, q):
                    
            #         lca = root
                    
            #     else:
                    
            #         return root

            # else: 
            #     leftVal =  lowestCommonAncestorHelper(root.left, p, q) 
            #     rightVal=lowestCommonAncestorHelper(root.right, p, q) 
            #     if not lca and leftVal and rightVal:
            #         lca = root

            #     elif leftVal and not rightVal:
            #         return leftVal
                
            #     elif not leftVal and rightVal:
            #         return rightVal


            
            
        lowestCommonAncestorHelper(root, p, q)
        return lca
