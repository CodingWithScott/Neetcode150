from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for curr_num in nums:
            if curr_num in seen:
                # print('Duplicates found')
                return True
            seen.add(curr_num)
        # print('No duplicates found')
        return False
    

# Should return true
nums = [1, 2, 3, 3]
solution = Solution()
print("This should be true: ")
print(solution.hasDuplicate(nums))

# Should return false
nums = [1, 2, 3, 4]
solution = Solution()
print("This should be false: ")
print(solution.hasDuplicate(nums))

