# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0;
        right = n;
        while (left < right):
            pivot = (right + left) // 2
            if (isBadVersion(pivot) == True):
                right = pivot
            if (isBadVersion(pivot) == False):
                left = pivot + 1
        return left    
            
        
            
        
        