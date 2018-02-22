from util import buildSequeneces
from util import printList

from solution import Solution

if __name__ == '__main__':
    sol = Solution()
    printList(sol.swapPairs(buildSequeneces([])))
    printList(sol.swapPairs(buildSequeneces([1])))
    printList(sol.swapPairs(buildSequeneces([1,2])))
    printList(sol.swapPairs(buildSequeneces([1,2,3])))
    printList(sol.swapPairs(buildSequeneces([1,2,3,4])))
    result = sol.swapPairs(buildSequeneces([1,2,3,4,5,6]))
    printList(result)