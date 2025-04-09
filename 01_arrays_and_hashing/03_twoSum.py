from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(f'nums: {nums}')
        print(f'target: {target}')
        for ix in range(0, len(nums)):
            for jx in range(ix+1, len(nums)):
                print('comparing: ')
                print(f'nums[{ix}]: {nums[ix]}')
                print(f'nums[{jx}]: {nums[jx]}')
                if (nums[ix] + nums[jx] == target):
                    print('Found solution!')
                    return [ix, jx]


solution = Solution()
nums = [3,4,5,6]
target = 7
print('Should return [0,1]: ' + str(solution.twoSum(nums, target)))

nums = [4,5,6]
target = 10
print('Should return [0,2]: ' + str(solution.twoSum(nums, target)))

nums = [-3,4,3,90]
target = 0
print('Should return [0,2]: ' + str(solution.twoSum(nums, target)))
