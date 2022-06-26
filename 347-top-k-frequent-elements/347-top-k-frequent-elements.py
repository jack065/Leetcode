class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        
        for i in nums:
            res[i] = 1 + res.get(i, 0)
            
        for n, c in res.items():
            freq[c].append(n)
            
        res = []
        
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        