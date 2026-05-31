class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[-1, -1]
        n=len(numbers)
        i, j=0, n-1
        while i<j:
            sm=numbers[i]+numbers[j]
            if sm==target: return [i+1, j+1]
            elif sm<target: i+=1
            else: j-=1
        