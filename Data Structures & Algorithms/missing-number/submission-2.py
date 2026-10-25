class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       length = len(nums)
       missing = {x : 0 for x in range(length + 2)}

       for n in nums:
        missing[n] = 1

       sol = -1

       for k,v in missing.items():
        if(v == 0):
            sol = k
            break
       
       return sol
