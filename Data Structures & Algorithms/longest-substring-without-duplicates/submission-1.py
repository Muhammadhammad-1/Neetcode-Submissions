class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        charSet = set()
        for i in range(len(s)):
            charSet.clear()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res,len(charSet))
            print(charSet)
        return res