from solution import ListNode
from solution import Solution


def buildSequeneces(seq):
    result = None
    for number in seq:
        if result is None:
            cur = ListNode(number)
            result = cur
        else:
            node = ListNode(number)
            cur.next = node
            cur = node
    return result

def printList(s1):
    p1 = s1
    while p1 is not None:
        if p1 is not s1:
            print ' -> ',
        print '%s' % p1.val,
        p1 = p1.next
    print '\n'

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
    