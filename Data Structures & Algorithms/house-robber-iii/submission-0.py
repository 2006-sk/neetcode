# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # Return (0, 0) for an empty node
            if not node:
                return (0, 0)
            
            # Recurse on left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If we rob this node, we cannot rob its direct children
            with_node = node.val + left[1] + right[1]
            
            # If we skip this node, we take the max possible from each child
            without_node = max(left) + max(right)
            
            return (with_node, without_node)
        
        # Take the best option between robbing or skipping the root
        return max(dfs(root))