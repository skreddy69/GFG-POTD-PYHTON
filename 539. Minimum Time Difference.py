class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # Convert each time into minutes from "00:00"
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(":"))
            minutes.append(h * 60 + m)
        
        # Sort the time points
        minutes.sort()
        
        # Initialize the minimum difference to a large value
        min_diff = float('inf')
        
        # Compare consecutive time points for minimum difference
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        # Handle wraparound: Compare the first and last time points
        # The difference is (1440 - last) + first (as if first was on the next day)
        min_diff = min(min_diff, 1440 + minutes[0] - minutes[-1])
        
        return min_diff