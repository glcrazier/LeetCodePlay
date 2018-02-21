from util import ListNode
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

    def longestPalindrome(self, s):
        l = len(s)
        rl = 0
        if l == 1:
            return s
        i = 0
        result = s[i]
        while i < (l - 1):
            j = i - 1
            k = i + 1
            check = False
            if s[i] == s[k]:
                while k < l and s[k] == s[i]:
                    k = k + 1
                check = True                  
            elif s[j] == s[k]:
                check = True
            if check == True:
                while j >= 0 and k < l:
                    if s[j] != s[k]:                         
                        break
                    j = j - 1
                    k = k + 1
                v = k - j - 1
                if rl < v:
                    result = s[j + 1:k]
                    rl = v     
            i = i + 1
        return result

    def mergeTwoLists(self, l1, l2):
        p1 = l1
        p2 = l2
        head = None
        c2 = None
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                cur = p1
                p1 = p1.next
            else:
                cur = p2
                p2 = p2.next
            if head == None:
                head = cur
                c2 = head
            else:
                c2.next = cur
                c2 = cur
        else:
            c3 = None
            if p1 is not None:
                c3 = p1
            if p2 is not None:
                c3 = p2
            if head is None:
                head = c3
            else:
                c2.next = c3 
        return head
                    
            
                
