class Solution:
    def getMinDiff(self, arr, k):
        # Sort the array
        arr.sort()
        n = len(arr)

        # Initialize result as current difference between max and min
        result = arr[-1] - arr[0]

        # Consider the case when we increase the smallest or decrease the largest
        smallest = arr[0] + k
        largest = arr[-1] - k

        # Traverse the array
        for i in range(n - 1):
            min_element = min(smallest, arr[i + 1] - k)
            max_element = max(largest, arr[i] + k)

            # If the min_element is negative, skip it
            if min_element < 0:
                continue

            result = min(result, max_element - min_element)

        return result