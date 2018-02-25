from solution import Solution

if __name__ == '__main__':
    sol = Solution()
    print sol.searchInsert([1,3,5,6], 5)
    print sol.searchInsert([1,3,5,6], 2)
    print sol.searchInsert([1,3,5,6], 7)
    print sol.searchInsert([1,3,5,6], 0)
    print ''
    print sol.searchInsert([], 0)
    print sol.searchInsert([1], 0)
    print sol.searchInsert([1], 2)
    print ''
    print sol.searchInsert([1,3], 2)
    print sol.searchInsert([1,3], 4)
    print ''
    print sol.searchInsert([1,3,5], 2)
    print sol.searchInsert([1,3,5], 4)
    print sol.searchInsert([1,3,5], 6)