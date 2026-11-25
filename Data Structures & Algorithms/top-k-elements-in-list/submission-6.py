class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = [] 

        freq = [[] for i in range(len(nums)+1)] #store how frequent each element appears 
        hashmap = {} 

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)
        
        for element,f in hashmap.items():
            freq[f].append(element) 
        
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        