from solution import Solution

if __name__ == '__main__':
   s = Solution()
   nums1 = [1, 2]
   nums2 = [3, 4]
   result = s.findMedianSortedArrays(nums1, nums2)
   print 'The median is %.1f' % result
    