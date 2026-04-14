class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        curr = 0
        longest = 0

        for n in numset:
            lenght = 1
            if (n - 1) not in numset:
                while (n + lenght) in numset:
                    lenght +=1
                
                longest = max(longest,lenght)
        return longest 