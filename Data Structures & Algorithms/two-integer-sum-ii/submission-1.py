class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        lp = 0
        rp = len(numbers) - 1

        while(lp < rp):
            if(numbers[lp] + numbers[rp]) > target:
                rp -= 1
            elif(numbers[lp] + numbers[rp]) < target:
                lp += 1
            else:
                result.append(lp + 1)
                result.append(rp + 1)
                break
        
        return result