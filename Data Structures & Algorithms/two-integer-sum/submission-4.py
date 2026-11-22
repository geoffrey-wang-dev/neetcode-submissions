class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return indices 

        hashmap = {} 

        for n in range(len(nums)):
            complement = target - nums[n]

            if complement in hashmap:
                return [hashmap.get(complement),n]
            
            hashmap[nums[n]] = n #store the index in the hashmap

            


