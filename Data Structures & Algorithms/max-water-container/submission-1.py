class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maximumWater = 0
        maxDistance = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                # width * height = area 
                # calculate width 
                width = j - i 
                currWater = min(heights[i],heights[j]) * width
                maximumWater = max(maximumWater,currWater)
        return maximumWater