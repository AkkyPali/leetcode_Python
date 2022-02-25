# https://leetcode.com/problems/palindrome-number/submissions/

#without converting to string solution

def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        if x < 10:
            return True
        num = x
        rev_num = 0
        while num > 0:
            a = num%10
            num = num//10
            rev_num = rev_num*10 + a
        if rev_num == x:
            return True

# Converting to string solution
if str(x) == str(x)[::-1]:
            return True

