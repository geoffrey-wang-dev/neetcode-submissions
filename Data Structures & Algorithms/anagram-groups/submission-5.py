class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        #loop through every word 
        for word in strs:
            count = [0] * 26 #made up of lowercase english letters 
            #loop through every letter 
            for char in word:
                count[ord(char) - ord('a')] += 1 

            res[tuple(count)].append(word)
            
        return list(res.values())
            

                
