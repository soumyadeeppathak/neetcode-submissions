class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        sol = []

        for i,n in enumerate(nums):
            valToCheck = target - n

            if(valToCheck in counter):
                sol.append(counter[valToCheck])
                sol.append(i)
            else:
                counter[n] = i
            
        
        return sol