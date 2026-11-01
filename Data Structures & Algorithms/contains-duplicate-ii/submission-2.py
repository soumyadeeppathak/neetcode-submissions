class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = r = 0
        check = {}

        while(r < len(nums)):
            if(abs(l-r) <= k and nums[r] not in check ):
                check[nums[r]] = 1
                r += 1
            elif(abs(l-r) > k):
                del check[nums[l]]
                l += 1
            elif(nums[r] in check):
                return True
        
        return False