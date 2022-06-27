class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        count = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            res[i] = 1 + res.get(i, 0)
            
        for n, c in res.items():
            count[c].append(n)
            
        result = []
            
        for i in range(len(count) -1, 0, -1):
            for n in count[i]:
                result.append(n)
                if len(result) == k:
                    return result
        