class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)

        sol = length*(length+1)/2

        for n in nums:
            sol -= n
        
        return int(sol)

        
        