class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        numRange = len(nums)

        for i in range(numRange):
            complement = target - nums[i]
            if complement in d:
                return [d[complement], i]
            d[nums[i]] = i
        
        return False