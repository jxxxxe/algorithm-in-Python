class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first,second=0,1
        while second < len(nums):
            if nums[first]!=nums[second]:
                first+=1
                nums[first]=nums[second]
                second+=1
                continue
            second+=1
        return first+1