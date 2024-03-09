class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        n = len(nums)
        l  = 0
        r = n-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                last = mid
                l = mid+1
        l = 0
        r = n-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                first = mid
                r = mid-1
        return [first, last]
