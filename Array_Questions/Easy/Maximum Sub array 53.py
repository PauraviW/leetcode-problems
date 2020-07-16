class Solution:
    def maximumSubArray(self, arr):
        low = 0
        high = len(arr) - 1
        return self.max_subarray(arr, low, high)


    def max_subarray(self, arr, low ,high):
        if high == low:
            return arr[high]
        mid = (low + high) // 2

        max_left = self.max_subarray(arr, low, mid)
        max_right = self.max_subarray(arr, mid + 1, high)
        max_center = self.max_crossing_array(arr, low, mid, high)
        return max(max_left, max_center, max_right)

    def max_crossing_array(self, arr, low, mid, high):

        left_sum = -float("inf")
        sum = 0
        print("here")
        for i in (range(mid, low - 1, -1)):
            sum = arr[i] + sum
            if sum > left_sum:
                left_sum = sum
        sum = 0
        right_sum = -float("inf")
        for i in range(mid+1, high+1):
            sum += arr[i]
            if sum > right_sum:
                right_sum = sum

        return left_sum + right_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
arr = [8,-19,5,-4,20]
print(Solution().maximumSubArray(arr))