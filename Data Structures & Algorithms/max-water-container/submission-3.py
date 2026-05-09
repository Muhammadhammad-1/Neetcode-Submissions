class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # take two pointer
        # from 0 and oen from end

        l = 0
        r = len(heights) - 1
        maximumWater = 0
        while l < r:
            # calculate the water
            print(f'index: {l} current Left num :{heights[l]}')
            print(f'index: {r} current right num :{heights[r]}')
            water = min(heights[l],heights[r]) * (r - l)  # heights * width
            if heights[l] < heights[r]:
                l +=1
            else:
                r -= 1
            maximumWater = max(water,maximumWater)
        return maximumWater