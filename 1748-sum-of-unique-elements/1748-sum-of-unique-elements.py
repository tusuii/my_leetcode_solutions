class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            if nums.count(i)==1:
                s=s+i
        return s