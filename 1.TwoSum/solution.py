import unittest

class Solution:
    def twoSum(self, nums, target):
        """Given an array of integers, return indices of the two numbers 
        such that they add up to a specific target. You may assume that 
        each input would have exactly one solution, and you may not use 
        the same element twice
        
        Arguments:
            nums {List[int]} -- List of integers
            target {int} -- The target for the addition
        
        Returns:
            List[int] -- List with the indices of the two numbers that 
            add up to the target
        """

        if len(nums) == 0:
            return 0

        result = [0, 0]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    result[0] = i
                    result[1] = j
                    return result

        return 0

        
class TestTwoSum(unittest.TestCase):
    
    def testEmpty(self):
        """Test the case when the input list is empty
        """

        solution = Solution()

        nums = []
        target = 1
        result = solution.twoSum(nums, target)
    
        self.assertEqual(result, 0)

    def testCase1(self):
        """Test the case when the input list has two elements
        """

        solution = Solution()

        nums = [1, 1]
        target = 2
        result = solution.twoSum(nums, target)

        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 1)
    
    def testCase2(self):
        """Test the case when the input list has more than two elements
        """

        solution = Solution()

        nums = [1, 1, 4, 5]
        target = 9
        result = solution.twoSum(nums, target)

        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 3)

if __name__ == '__main__':
    unittest.main()