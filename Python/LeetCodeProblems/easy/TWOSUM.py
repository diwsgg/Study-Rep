class Solution:
    def twoSum3(self, nums: list[int], target: int) -> list[int]:
        #Empty dict
        allNumbers = {}
        for index, num in enumerate(nums):
            remainder = target-num
            if remainder in allNumbers:
                return [allNumbers[remainder], index]
            allNumbers[num] = index 
sol3 = Solution()



print(sol3.twoSum3([2,7,11,15], 9))

print(sol3.twoSum3([3,2,4], 6))

print(sol3.twoSum3([3,3], 6))