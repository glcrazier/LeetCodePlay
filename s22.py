from solution import Solution
from util import printList

def printStringList(param):
    for r in param:
        print '%s' % r

if __name__ == '__main__':
    sol = Solution()
    for i in range(0, 5):
        print 'testing arg %s' % i
        printStringList(sol.generateParenthesis(i))
