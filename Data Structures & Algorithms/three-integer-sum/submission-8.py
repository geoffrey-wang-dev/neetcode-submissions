class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() 
        res = [] 

        for n in range(len(nums)):
            #edge case if first element is greater than 0, it's not possible for the sum to be 0 
            if nums[n] > 0:
                break 

            #edge case if element is not the first one and it's a duplicate move onto the next loop
            if n > 0 and nums[n-1]==nums[n]:

                continue
            
            a = nums[n]
            left = n + 1
            right = len(nums)-1
            while left < right:

                total_sum = a + nums[left] + nums[right]

                if total_sum == 0:
                    res.append([a,nums[left],nums[right]])
                    left += 1 
                    right -= 1 
                    #edge case:avoid duplicates 
                    while left<right and nums[left] == nums[left-1]:
                        left += 1 
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1 

                elif total_sum > 0:
                    right -= 1
                else:
                    left += 1 
        
        return res 
            

