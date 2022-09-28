class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)
        def gcd(b,a):
            while a!=b:
                if a>b:
                    a=a-b
                else:
                    b=b-a
            return a
        return gcd(a,b)