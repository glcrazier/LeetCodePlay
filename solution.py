from util import ListNode
from util import printList
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
                    
    def maxArea(self, height):
        start = 0
        end = len(height)
        result = 0
        q = [(start, end)]
        def maxSearch(s, e): 
            i = s + 1
            area = 0
            a2 = 0
            while i < e:
                if height[i] >= height[s]:
                    area = (i - s) * height[s]
                    break
                i = i + 1
            else:
                if s + 1 < e:
                    area = height[s + 1]
            if i < e:
                q.append((i, e))
            return area

        while len(q) > 0:
            arg = q[0]
            q = q[1:]
            v = maxSearch(arg[0], arg[1])
            if v > result:
                result = v
        return result
            
    def maxArea2(self, height):
        i = 0
        j = len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water       

    def swapPairs(self, head):
        vhead = ListNode(0)
        vhead.next = head
        left = vhead
        middle = head
        right = None
        while middle is not None:
            right = middle.next
            if right is None:
                break
            middle.next = right.next
            left.next = right
            right.next = middle
            left = middle
            middle = left.next
        return vhead.next

    def reverseKGroup(self, head, k):
        if k < 2:
            return head
        vhead = ListNode(0)
        vhead.next = head
        #search for next k nodes
        def hasNodes(nodeHead, numNodes):
            c = nodeHead.next
            while numNodes > 0:
                if c is None:
                    return False
                c = c.next
                numNodes = numNodes - 1
            return True
        def reverseNodes(nodeHead, numNodes):
            c0 = nodeHead
            c1 = c0.next
            c2 = c1.next
            c3 = c1
            n = numNodes - 1
            while n > 0:
                t = c2.next
                c2.next = c1
                c0.next = c2
                c1 = c2
                c2 = t 
                n = n - 1
            c3.next = t
            return c3
        cur = vhead
        while hasNodes(cur, k) is True:
            cur = reverseNodes(cur, k)
        return vhead.next

    def removeElement(self, nums, val):
        if nums is None:
            return 0
        dupCount = 0
        i = 0
        l = len(nums)
        while i < l:
            nums[i] = nums[i + dupCount]
            if nums[i] == val:
                l = l - 1
                dupCount = dupCount + 1
                i = i - 1
            i = i + 1
        return l

    def longestValidParentheses(self, s):
        lc = 0
        rc = 0
        maxl = 0
        d = 0
        pos = 0
        length = len(s)
        while pos < length:
            i = s[pos]
            if i == '(':
                lc = lc + 1
            elif i == ')':
                rc = rc + 1
                d = lc - rc
                if d < 0:
                    if lc > maxl:
                        maxl = lc
                    rc = 0
                    lc = 0
                elif d >= 1:
                    lc1 = d
                    rc1 = 0
                    if pos == len(s) - 1:
                        if rc - 1 > maxl:
                            maxl = rc - 1
                        elif maxl < 1:
                            maxl = 1
                        lc = rc = 0
                    else:
                        j = pos + 1
                        while j < length:
                            if s[j] == '(':
                                lc1 = lc1 + 1
                            else:
                                rc1 = rc1 + 1
                            if lc1 == rc1:
                                break
                            j = j + 1
                        if lc1 != rc1:
                            if rc - 1 > maxl:
                                maxl = rc - 1
                            elif maxl < 1:
                                maxl = 1
                            lc = rc = 0
                            pos = pos - d - 1
                        else:
                            rc = rc1 + rc
                            lc = rc
                            pos = j
            pos = pos + 1
        if lc >= rc:
            if rc > maxl:
                maxl = rc
        return maxl * 2
                        
                


