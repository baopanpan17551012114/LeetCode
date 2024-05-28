from typing import List


class Solution:
    def quick_sort(self, nums, left, right):
        value = nums[left]
        while left < right:
            print(left, right)
            while nums[right] >= value and left < right:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            while nums[left] <= value and left < right:
                left += 1
            nums[left], nums[right] = nums[right], nums[left]
        return left

    def majorityElement(self, nums: List[int]) -> int:
        target_index = int(len(nums) / 2)
        left = 0
        right = len(nums) - 1
        while left < right:
            index = self.quick_sort(nums, left, right)
            if index <= target_index:
                return nums[index]
            else:
                right = index - 1


if __name__ == '__main__':
    # li = [2,2,1,1,1,2,2]
    # res = Solution().majorityElement(li)
    # print(res)
    print(2 ** 31-1)