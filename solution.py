class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        pL1 = l1
        pL2 = l2
        addOneDigit = False
        result = None
        cur = None
        while pL1 is not None and pL2 is not None:
            val = pL1.val + pL2.val;
            if addOneDigit is True:
                val = val + 1
                addOneDigit = False
            if val >= 10:
                addOneDigit = True
                val = val - 10
            n = ListNode(val)
            if result is None:
                result = n
            else:
                cur.next = n
            cur = n
            pL1 = pL1.next
            pL2 = pL2.next
        if pL1 is not None:
            cur.next = pL1
        if pL2 is not None:
            cur.next = pL2
        while addOneDigit is True:
            t = cur
            cur = cur.next
            if cur is None:
                node = ListNode(1)
                t.next = node
                addOneDigit = False
            else:
                val = cur.val + 1
                if val >= 10:
                    cur.val = val - 10
                    addOneDigit = True
                else:
                    addOneDigit = False
                    cur.val = val
        return result
    
    def findMedianSortedArrays(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        aux = []
        p1 = 0
        p2 = 0
        while p1 < l1 and p2 < l2:
            if nums1[p1] < nums2[p2]:
                aux.append(nums1[p1])
                p1 = p1 + 1
            else:
                aux.append(nums2[p2])
                p2 = p2 + 1
        if p1 < l1:
            aux.extend(nums1[p1:])
        elif p2 < l2:
            aux.extend(nums2[p2:])
        l = l1 + l2
        if l % 2 == 0:
            r = l / 2
            return (aux[r - 1] + aux[r]) / 2.0
        else:
            return aux[(l - 1) / 2]
