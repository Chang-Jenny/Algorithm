class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict={}
        for i in range(len(nums)):
            if numDict.__contains__(target-nums[i]):
                return [numDict.get(target-nums[i]), i]
            else:
                numDict[nums[i]]=i
