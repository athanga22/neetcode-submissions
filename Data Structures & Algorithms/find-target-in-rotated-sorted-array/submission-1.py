class Solution:
    def binary_search(self, nums: List[int], l: int, r: int, target: int) -> int:
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target: return mid
            elif nums[mid]<target: l=mid+1
            else: r=mid-1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l, r=0, len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        
        pivot=l
        idx=self.binary_search(nums, 0, pivot-1, target)
        if idx!=-1: return idx
        return self.binary_search(nums, pivot, len(nums)-1, target)
        