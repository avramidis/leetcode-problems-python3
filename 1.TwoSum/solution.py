
class Solution:
    def twoSumBruteForce(self, nums, target):
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

        Algorithm analysis:
            Run-time complexity -- It is O(n^2) taken from n(n+1)/2. This 
            is based on the Gauss formula for calculating the sum of the
            series of numbers 1+2+3+...+n
            Storage complexity -- O(1)
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

    def twoSumTwoPassHashTable(self, nums, target):
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

        Algorithm analysis:
            Run-time complexity -- It is O(n) for 2*n because we iterate
            the nums list twice. One to add the data and one to search.
            Storage complexity -- O(n) because we add each element of num
            to a dictionary.
        """

        if len(nums) == 0:
            return 0

        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]]=i

        for i in range(len(nums)):
            num2 = target - nums[i]
            if (num2 in hashmap and hashmap[num2]!=i):
                return [i, hashmap[num2]]

        return 0

    def twoSumOnePassHashTable(self, nums, target):
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

        Algorithm analysis:
            Run-time complexity -- It is O(n) because we iterate the 
            nums at most once.
            Storage complexity -- O(n) because we add each element of num
            to a dictionary.
        """

        if len(nums) == 0:
            return 0

        hashmap = {}

        for i in range(len(nums)):
            num2 = target - nums[i]
            if (num2 in hashmap):
                return [hashmap[num2],i]
            hashmap[nums[i]]=i

        return 0

    
def testEmpty():
    """Test the case when the input list is empty
    """

    solution = Solution()

    nums = []
    target = 1
    result = solution.twoSumBruteForce(nums, target)
    assert (result == 0)

    result = solution.twoSumTwoPassHashTable(nums, target)
    assert (result == 0)

    result = solution.twoSumOnePassHashTable(nums, target)
    assert (result == 0)

def testCase1():
    """Test the case when the input list has two elements
    """

    solution = Solution()

    nums = [1, 1]
    target = 2
    result = solution.twoSumBruteForce(nums, target)
    assert (result[0] == 0)
    assert (result[1] == 1)

    result = solution.twoSumTwoPassHashTable(nums, target)
    assert (result[0] == 0)
    assert (result[1] == 1)

    result = solution.twoSumOnePassHashTable(nums, target)
    assert (result[0] == 0)
    assert (result[1] == 1)

def testCase2():
    """Test the case when the input list has more than two elements
    """

    solution = Solution()

    nums = [1, 1, 4, 5]
    target = 9
    result = solution.twoSumBruteForce(nums, target)
    assert (result[0] == 2)
    assert (result[1] == 3)

    result = solution.twoSumTwoPassHashTable(nums, target)
    assert (result[0] == 2)
    assert (result[1] == 3)

    result = solution.twoSumOnePassHashTable(nums, target)
    assert (result[0] == 2)
    assert (result[1] == 3)
