class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       sol = [0,0]
       lptr = 0
       rptr =  len(numbers) - 1

       while(lptr < rptr):
            check = numbers[lptr] + numbers[rptr]

            if(check > target):
                rptr -= 1
            elif(check < target):
                lptr += 1
            else:
                sol[0] = lptr + 1
                sol[1] = rptr + 1
                break
       return sol