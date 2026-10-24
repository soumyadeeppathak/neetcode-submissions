class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missingList = []
        positionsFilled = {}
        length = len(nums)

        for n in nums:
            if(n not in positionsFilled):
                positionsFilled[n] = 1
        
        for i in range(1, length + 1):
            if(i not in positionsFilled):
                missingList.append(i)
        

        return missingList