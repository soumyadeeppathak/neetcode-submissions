class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d: dict[int,int] = {}
        sol = []
        for i,n in enumerate(nums):
            lookout = target - n
            if lookout in d:
                if i<d[lookout]:
                    sol.append(i)
                    sol.append(d[lookout])
                else:
                    sol.append(d[lookout])
                    sol.append(i)
                return sol
            else:
                d[n] = i