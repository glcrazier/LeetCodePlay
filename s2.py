from solution import Solution
from util import *

def printResult(s1, s2, result):
    print 'Input:\n'
    printList(s1)
    printList(s2) 
    print 'Output:\n'
    printList(result)
            

def main():
    s1 = buildSequeneces([2, 4, 3, 9])
    s2 = buildSequeneces([5, 6, 6])
    sol = Solution()
    result = sol.addTwoNumbers(s1, s2)
    printResult(s1, s2, result)
    pass

if __name__ == '__main__':
    main()
    