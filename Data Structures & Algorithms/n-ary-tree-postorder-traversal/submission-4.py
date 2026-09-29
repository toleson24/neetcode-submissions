"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack = [root]
        order = []
        
        while stack:
            node = stack.pop(-1)
            order.append(node.val)
            for child in node.children:
                stack.append(child)

        order.reverse()
        return order
        
        