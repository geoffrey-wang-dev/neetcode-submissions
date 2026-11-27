class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0 #return value 

        left = 0
        right = len(heights) - 1 

        while left < right:
            
            #area = length x width 
            #need the max height of both sides for height
            #need the difference for length
            currArea = (right-left) * min(heights[left],heights[right])
            maxArea = max(currArea,maxArea)

            #find container with the highest height

            if heights[left] < heights[right]:
                left += 1 
            else:
                right -= 1 
        
        return maxArea
