class Solution:
    def hasDuplicate(self,nums: List[int])-> bool:
        #
        # take a set
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            else:
                hashmap[nums[i]]=i
        return False
