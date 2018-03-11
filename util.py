class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[%d, %d]' % (self.start, self.end)

    def __repr__(self):
        return self.__str__()
        
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