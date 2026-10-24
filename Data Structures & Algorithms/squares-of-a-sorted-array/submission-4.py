class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        initialPointer = 0
        lastPointer = len(nums) - 1
        sol = []

        while(initialPointer < lastPointer):
            val1 = nums[initialPointer] ** 2
            val2 = nums[lastPointer] ** 2

            if(val1 > val2):
                sol.insert(0, val1)
                initialPointer += 1
            else:
                sol.insert(0, val2)
                lastPointer -= 1
        
        sol.insert(0, nums[initialPointer] ** 2)

        return sol