from solution import Solution
from util import Interval

if __name__ == '__main__':
    sol = Solution()
    intervals = []
    intervals.append(Interval(1,3))
    intervals.append(Interval(8,10))
    intervals.append(Interval(2,6))
    intervals.append(Interval(15,18))
    print sol.merge(intervals)

    intervals = []
    intervals.append(Interval(1,3))
    intervals.append(Interval(1,3))
    intervals.append(Interval(1,2))
    intervals.append(Interval(2,6))
    intervals.append(Interval(15,18))
    print sol.merge(intervals)

    intervals = []
    print sol.merge(intervals)

    intervals = []
    intervals.append(Interval(1,3))
    print sol.merge(intervals)

    intervals = []
    intervals.append(Interval(1,3))
    intervals.append(Interval(1,2))
    print sol.merge(intervals)
    
    intervals = []
    intervals.append(Interval(1,2))
    intervals.append(Interval(1,3))
    print sol.merge(intervals)