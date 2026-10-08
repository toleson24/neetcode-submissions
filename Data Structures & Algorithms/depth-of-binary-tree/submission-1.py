# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dive(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1

            curr_depth = 0
            curr_depth += max(dive(root.left), dive(root.right)) + 1

            return curr_depth
        
        return dive(root)

        