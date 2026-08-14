# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        heights = {None: 0}
        temp_tree = [(root, False)]
        mxs = []
        
        while temp_tree:
            dummy, expanded = temp_tree.pop()
            if dummy is None:
                continue

            if not expanded:
                temp_tree.append((dummy, True))
                temp_tree.append((dummy.left, False))
                temp_tree.append((dummy.right, False))
            
            else:
                left, right = heights[dummy.left], heights[dummy.right]
                mxs.append(left + right)
                heights[dummy] = 1 + max(left, right)
                
        return max(mxs) if mxs else 0

            