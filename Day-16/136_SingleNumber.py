class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=Counter(nums)
        for i,j in count.items():
            if j<2:
                return i
