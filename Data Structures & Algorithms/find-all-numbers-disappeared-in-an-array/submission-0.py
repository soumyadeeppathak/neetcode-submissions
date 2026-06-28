class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d: dict[int,int] = {}
        sol = []

        for i in range(len(nums)):
            d[i+1] =  0
        
        for n in nums:
            d[n] = d[n]+1;
        
        for n in d:
            if d[n] == 0:
                sol.append(n)
        

        return sol

        