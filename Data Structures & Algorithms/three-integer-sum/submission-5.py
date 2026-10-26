class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        sol = []
        end = len(nums) - 1

        for i,n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = n * (-1)
            lptr = i+1
            rptr = end

            while(lptr < rptr):
                check = nums[lptr] + nums[rptr]

                if(check < target):
                    lptr += 1
                elif(check > target):
                    rptr -= 1
                else:
                    sol.append([nums[i], nums[lptr], nums[rptr]])
                    while(lptr < rptr and nums[lptr] == nums[lptr+1]):
                        lptr += 1
                    while(lptr < rptr and nums[rptr] == nums[rptr-1]):
                        rptr -= 1
                    lptr += 1
                    rptr -= 1
                    
        return sol

