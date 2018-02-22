from solution import Solution

if __name__ == '__main__':
    sol = Solution()
    l = [3, 2, 2, 3, 2, 3, 3, 4, 5, 6]
    print sol.removeElement(l, 3)
    print l

    l = [3, 2, 2, 3, 2, 1, 3, 3, 4, 5, 6]
    print sol.removeElement(l, 1)
    print l
    
    