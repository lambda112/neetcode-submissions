class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = dict({})

        for index, value in enumerate(nums):
            difference = target - value

            if difference in nums_hash.keys():
                return [nums_hash[difference],index]

            nums_hash[value] = index


            
