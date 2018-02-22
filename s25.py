from util import ListNode
from util import buildSequeneces
from util import printList
from solution import Solution

if __name__ == '__main__':
    sol = Solution()
    for i in range(0, 8):
        printList(sol.reverseKGroup(buildSequeneces([1, 2, 3, 4, 5]), i))

    for i in range(0, 2):
        printList(sol.reverseKGroup(buildSequeneces([]), i))
    
    k = 1
    for i in range(0, k + 2):
        printList(sol.reverseKGroup(buildSequeneces(list(range(1, 2))), i))
    