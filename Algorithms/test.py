# A divide and conquer program in Python3
# to find the smallest distance from a
# given set of points.

import math


# A class to represent a Point in 2D plane


    # A utility function to find the


# distance between two points

def dist(p1, p2):
    return (p1[0] - p2[0])**2+(p1[1] - p2[1]) **2




# A Brute Force method to return the
# smallest distance between two points
# in P[] of size n

def bruteForce(P, n):
    min_val = float('inf')

    for i in range(n):

        for j in range(i + 1, n):

            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])

    return min_val


# A utility function to find the
# distance beween the closest points of
# strip of given size. All points in
# strip[] are sorted accordint to
# y coordinate. They all have an upper
# bound on minimum distance as d.
# Note that this method seems to be
# a O(n^2) method, but it's a O(n)
# method as the inner loop runs at most 6 times

def stripClosest(strip, size, d):
    # Initialize the minimum distance as d

    min_val = d

    strip.sort(key=lambda point: point[1])

    # Pick all points one by one and

    # try the next points till the difference

    # between y coordinates is smaller than d.

    # This is a proven fact that this loop

    # runs at most 6 times

    for i in range(size):

        j = i + 1

        while j < size and (strip[j][1] -strip[i][1]) < min_val:
            min_val = dist(strip[i], strip[j])

            j += 1

    return min_val


# A recursive function to find the
# smallest distance. The array P contains
# all points sorted according to x coordinate

def closestUtil(P, n):
    # If there are 2 or 3 points,

    # then use brute force

    if n <= 3:
        return bruteForce(P, n)

        # Find the middle point

    mid = n // 2

    midPoint = P[mid]

    # Consider the vertical line passing

    # through the middle point calculate

    # the smallest distance dl on left

    # of middle point and dr on right side

    dl = closestUtil(P[:mid], mid)

    dr = closestUtil(P[mid:], n - mid)

    # Find the smaller of two distances

    d = min(dl, dr)

    # Build an array strip[] that contains

    # points close (closer than d)

    # to the line passing through the middle point

    strip = []

    for i in range(n):

        if abs(P[i][0] - midPoint[0]) < d:
            strip.append(P[i])

            # Find the closest points in strip.

    # Return the minimum of d and closest

    # distance is strip[]

    return min(d, stripClosest(strip, len(strip), d))


# The main function that finds
# the smallest distance.
# This method mainly uses closestUtil()

def closest(P, n):
    P.sort(key=lambda point: point[0])

    # Use recursive function closestUtil()

    # to find the smallest distance

    return closestUtil(P, n)


# Driver code
P = [(77, 0), (1000, 1000),

     (992, 500), (1000000, 0),

     ]
n = len(P)

print("The smallest distance is",

      closest(P ,n))

# This code is contributed
# by Prateek Gupta (@prateekgupta10)