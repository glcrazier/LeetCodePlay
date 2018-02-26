from solution import Solution
from util import buildSequeneces
from util import printList

if __name__ == '__main__':
    sol = Solution()
    printList(sol.rotateRight(buildSequeneces([1,2,3,4,5]), 0))
    printList(sol.rotateRight(buildSequeneces([1,2,3,4,5]), 1))
    printList(sol.rotateRight(buildSequeneces([1,2,3,4,5]), 2))
    printList(sol.rotateRight(buildSequeneces([1,2,3,4,5]), 3))
    printList(sol.rotateRight(buildSequeneces([1,2,3,4,5]), 4))
    printList(sol.rotateRight(buildSequeneces([1,2,3,4,5]), 5))
    printList(sol.rotateRight(buildSequeneces([]), 5))
    printList(sol.rotateRight(buildSequeneces([1]), 5))
    printList(sol.rotateRight(buildSequeneces([1,2]), 1))
    printList(sol.rotateRight(buildSequeneces([1,2]), 2))
    printList(sol.rotateRight(buildSequeneces([1,2]), 3))

    