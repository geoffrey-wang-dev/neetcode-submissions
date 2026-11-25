class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #return value 
        res = []

        #list of frequencys of each element
        freq = [[] for i in range(len(nums)+1)]

        hashmap = {} #count the frequencies of each element 

        
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)

        for element,count in hashmap.items():
            freq[count].append(element)

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res 
