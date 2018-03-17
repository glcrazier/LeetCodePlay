from solution import Solution
import time

if __name__ == '__main__':
    sol = Solution()
    print sol.divide(1, 0)
    print sol.divide(1, 5)
    print sol.divide(0, 5)
    print sol.divide(5, 5)
    print sol.divide(7, 5)
    print sol.divide(10, 5)
    print sol.divide(10, -5)
    print sol.divide(-10, 5)
    print sol.divide(-10, -5)
    t = time.time()
    print sol.divide(-2147483648, -1)
    t = time.time() - t
    print "cost %d" % (t * 1000)
    