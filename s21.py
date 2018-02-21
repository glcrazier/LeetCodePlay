from solution import Solution
from util import buildSequeneces
from util import printList
if __name__ == '__main__':
    sol = Solution()
    l1 = buildSequeneces([1, 2, 4])
    l2 = buildSequeneces([1, 3, 4])
    printList(sol.mergeTwoLists(l1, l2))
    l1 = buildSequeneces([])
    l2 = buildSequeneces([1, 2, 5])
    printList(sol.mergeTwoLists(l1, l2))
    l2 = buildSequeneces([])
    printList(sol.mergeTwoLists(l1, l2))
    