# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #I think I need to measure depth as well, because I will keep it as a right then left thing so if it goes right then i append that, if it still goes right I append that, and then I do that until we get to the leaf. so for each tree i cehck right then if not in right then left. 
        result = []
        count = 0
        def s(node, depth):
            if not node:
                return
            
            if depth == len(result):
                result.append(node.val)
            # go right FIRST so the rightmost node at each level is seen first
            s(node.right, depth + 1)
            s(node.left, depth + 1)
                
        
        s(root,0)
        return result

        