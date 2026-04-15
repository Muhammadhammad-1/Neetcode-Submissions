class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr =''
        for i in s:
            if i.isalnum():
                newStr += i.strip().lower()
        print(newStr)
        print(newStr[::-1])
        if newStr == newStr[::-1]:
            return True
        return False
