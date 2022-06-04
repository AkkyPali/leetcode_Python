class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        right_bound = len(s)
        left_bound = len(t)
        
        r = 0
        l = 0
        yes = 0 
        while l < left_bound and r < right_bound:
            print (r, l)
            if s[r] == t[l]:
                yes = yes + 1
                r = r+ 1
                l = l+1
            else:
                l = l + 1
        if yes == len(s):
            return True
        
