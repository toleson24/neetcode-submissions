"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.traversal = []

    def traverse(self, root: 'Node'):
        if root == None:
            return
        
        if root.children == None:
            return root.val
        
        for child in root.children:
            self.traverse(child)
        
        self.traversal.append(root.val)

    def postorder(self, root: 'Node') -> List[int]:
        # print(self.traversal)
        self.traverse(root)
        return self.traversal
        
        