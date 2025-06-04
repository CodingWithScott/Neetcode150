'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
'''

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key = element, value = # of occurrences
        seen_counter = {}

        # Populate dict with number of occurrences of each element in nums
        for curr_num in nums:
            if seen_counter.get(curr_num):
                seen_counter[curr_num] += 1
            else:
                seen_counter[curr_num] = 1

        print('seen_counter:')
        print(seen_counter)

        # Store dict as a list of tuples
        tuple_list = list(seen_counter.items())
        print('tuple_list:')
        print(tuple_list)
        # Sort list of tuples based on second element (occurrence counter)
        sorted_tuples = sorted(tuple_list, key=lambda x: x[1])
        print('sorted_tuples:')
        print(sorted_tuples)

        # Print the last K entries in the list to verify
        print('sorted_tuples[len(sorted_tuples)-k:]:')
        print(sorted_tuples[len(sorted_tuples)-k:])

        # Return the list of top K most frequently occurring nums
        output = []
        for curr_tuple in sorted_tuples[len(sorted_tuples)-k:]:
            output.append(curr_tuple[0])

        print('output:')
        print(output)

        return output




sol = Solution()

nums1 = [1,2,2,3,3,3]
# nums1 = [4,5,5,6,6,6]
k = 2
valid_output = [2,3]
output1 = sol.topKFrequent(nums1, k)

# nums2 = [7, 7]
# k = 1
# valid_output2 = [7]
# output2 = sol.topKFrequent(nums2, k)


