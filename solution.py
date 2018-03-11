from util import ListNode
from util import printList
from util import Interval
import time
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
    def permuteUnique(self, nums):
        pass

    def searchInsert(self, nums, target):
        i = 0
        j = len(nums) - 1
        while i <= j:
            m = i + (j - i) / 2
            v = nums[m]
            if v == target:
                return m
            elif target > v:
                i = m + 1
            else:
                j = m - 1
        return i    
                
    def combinationSum(self, candidates, target):
        result = []
        length = len(candidates)
        def backtrack(a, k, t):
            if t == 0:
                result.append(a)
                return 
            if t < 0:
                return
            j = k
            la = len(a)
            while j < length:
                c = candidates[j]
                r = t - c
                if r == 0:
                    s = list(a)
                    s.append(c)
                    result.append(s)
                elif r > 0:
                    a.append(c)
                    backtrack(a, j, r)
                    a = a[:la]
                j = j + 1
        i = 0
        while i < length:
            backtrack([candidates[i]], i, target - candidates[i])
            i = i + 1
        return result
    
    def combinationSum2(self, candidates, target):
        result = []
        length = len(candidates)
        candidates = sorted(candidates)
        def backtrack(a, k, t):
            if t == 0:
                result.append(a)
                return 
            if t < 0:
                return
            j = k + 1
            la = len(a)
            lac = -1
            while j < length:
                c = candidates[j]
                if c == lac:
                    j = j + 1
                    continue
                lac = c
                r = t - c
                if r == 0:
                    s = list(a)
                    s.append(c)
                    result.append(s)
                elif r > 0:
                    a.append(c)
                    backtrack(a, j, r)
                    a = a[:la]
                j = j + 1
        i = 0
        last = -1
        while i < length:
            cur = candidates[i]
            if last != cur:
                backtrack([cur], i, target - cur)
            last = cur
            i = i + 1
        return result   

    def firstMissingPositive(self, nums):
        l = len(nums)
        vector = [0] * l
        for i in nums:
            if i <= l and i >= 1:
                vector[i - 1] = 1
        j = 0
        while j < l:
            if vector[j] == 0:
                return j + 1;
            j = j + 1
        return l + 1

    def myPow(self, x, n):
        if n == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        if n % 2 == 0:
            s = self.myPow(x, n/2)
            return s * s
        else:
            s1 = self.myPow(x, n/2)
            s2 = s1 * x
            return s1 * s2
    def rotateRight(self, head, k):
        # reverse
        if k == 0 or head is None:
            return head
        c = head
        n = c.next
        l = 1
        while n is not None:
            s = n.next
            n.next = c
            c = n
            n = s
            l = l + 1
        head.next = None
        head = c
        # count k
        k = k % l
        j = 0
        findK = None
        findK3 = None
        while j < k:
            findK3 = c
            findK = c.next
            c = c.next
            j = j + 1
        findK2 = head
        # reverse again
        c = head
        n = c.next
        while n is not None:
            s = n.next
            n.next = c
            c = n
            n = s
        head.next = None
        head = c
        # rotate
        if k != 0:
            findK2.next = head
            findK.next = None
        else:
            return head
        return findK3

    def threeSum(self, nums):
        nums = sorted(nums)
        nlen = len(nums)
        i = 0
        if nlen < 3:
            return []
        mk1 = 0
        mk2 = nlen - 1
        lastNum = nums[-1]
        while mk1 <= mk2:
            md = mk1 + (mk2 - mk1) / 2
            if nums[md] == 0:
                mk1 = md
                break
            elif nums[md] > 0:
                mk2 = md - 1
            else:
                mk1 = md + 1
        indexOfFirstNonNegative = mk1
        if mk1 > mk2:
            indexOfFirstNonNegative = mk2
        last = nums[0] - 1
        result = []
        while i < nlen:
            cur = nums[i]
            if cur > 0:
                break
            if last == cur:
                i = i + 1
                continue
            last = cur
            j = i + 1
            if -cur > lastNum:
                j = indexOfFirstNonNegative
            maxj = nlen
            lastj = nums[0] - 1
            lastmd = nlen - 1
            while j < maxj:
                curj = nums[j]
                target = curj + cur
                if target > 0:
                    break
                if lastj == curj:
                    j = j + 1
                    continue
                lastj = curj
                target = -target
                if target > lastNum:
                    j = j + 1
                    continue
                if target < curj:
                    break
                tk1 = j + 1
                if tk1 < indexOfFirstNonNegative:
                    tk1 = indexOfFirstNonNegative
                tk2 = lastmd
                while tk1 <= tk2:
                    md = tk1 + (tk2 - tk1) / 2
                    mdd = nums[md]
                    if target == mdd:
                        result.append([cur, curj, mdd])
                        lastmd = md - 1
                        break
                    elif target > mdd:
                        tk1 = md + 1
                    else:
                        tk2 = md - 1
                j = j + 1 
            i = i + 1
        return result
                
    def jump(self, nums):
        nlen = len(nums)
        result = [0] * nlen 
        i = 0
        while i < nlen:
            maxj = nums[i]
            j = 1
            cur = result[i]
            while j <= maxj:
                idx = i + j
                if idx >= nlen:
                    break
                c = cur + 1
                if result[idx] > c or result[idx] == 0:
                    result[idx] = c
                j = j + 1
            i = i + 1
        return result[-1]

    def lengthOfLastWord(self, s):
        lastLength = 0
        reset = False
        for c in s:
            if c == ' ':
                reset = True
            else:
                if reset is True:
                    lastLength = 0
                    reset = False
                lastLength = lastLength + 1
        return lastLength

    def canJump(self, nums):
        queue = []
        queue.append(0)
        con = len(nums) - 1
        records = [False] * len(nums)
        records[0] = True
        while len(queue) > 0:
            # print queue
            pos = queue.pop()
            num = nums[pos]
            if pos + num >= con:
                return True
            for i in range(1, num + 1):
                if records[pos + i] == False:
                    queue.append(pos + i)
                    records[pos + i] = True
        return False

    def merge(self, intervals):
        intervals.sort(cmp=lambda x,y: cmp(x.start,y.start))
        i = 1
        result = []
        length = len(intervals)
        if length == 0:
            return result
        current = intervals[0]
        while i < length:
            nex = intervals[i]
            if nex.start > current.end:
                result.append(current)
                current = nex
            elif nex.end > current.end:
                current.end = nex.end
            i = i + 1
        result.append(current)
        return result