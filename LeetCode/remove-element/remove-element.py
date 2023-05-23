class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index=0
        for i,n in enumerate(nums):
            if n==val:
                index+=1
                continue
            nums[i-index]=n
            
        return len(nums)-index