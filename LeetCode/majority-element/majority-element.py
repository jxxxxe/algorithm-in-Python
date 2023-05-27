class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=len(nums)

        while True:
            max_num=max(nums)
            if nums.count(max_num) < count/2:
                nums.remove(max_num)
            else:
                return max(nums)