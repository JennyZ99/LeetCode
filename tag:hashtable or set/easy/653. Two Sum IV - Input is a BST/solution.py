"""
time complexity: O(n) where n is the number of nodes. 
** or I also can use Master Theorem to get the time complexity of BST traversal.

I use recursion for this problem. 

data structure: set
            -- the set is used for store the remains, where a remain = (k - seen_val)
            -- and if unseen_val is in the set, we return True
            
** as we need update the set in each recursion, I create a new function. 

"""

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        myset = set()
        if root!=None: 
            return self.find(root, myset, k)
        return False
    
    def find(self, root: Optional[TreeNode], myset: set, k:int) -> bool:
        if root!=None:
            if root.val in myset: return True
            r = k - root.val
            myset.add(r)
            return self.find(root.left, myset, k) or self.find(root.right, myset, k)
        return False
