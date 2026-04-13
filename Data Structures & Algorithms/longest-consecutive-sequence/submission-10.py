class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sorted_nums= sorted(nums)
        hashset = set(nums)
        currentSeq = 0
        longestSeq = 0
    
        for n in hashset:

            if (n - 1) not in hashset:
                lenght = 1

                while (n + lenght) in hashset:
                    lenght += 1

                longestSeq = max(longestSeq, lenght)

        return longestSeq
            
            
