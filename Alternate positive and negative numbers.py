class Solution:
    def rearrange(self, arr):
        # Separate positive (including zero) and negative numbers
        positive = []
        negative = []
        
        for num in arr:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)
        
        # Now, we have two separate lists: positive and negative
        i, j = 0, 0
        index = 0
        flag = True
        
        # Alternating between positive and negative lists and modifying arr in place
        while i < len(positive) and j < len(negative):
            if flag:
                arr[index] = positive[i]
                i += 1
            else:
                arr[index] = negative[j]
                j += 1
            index += 1
            flag = not flag
        
        # If there are remaining positive numbers, append them
        while i < len(positive):
            arr[index] = positive[i]
            i += 1
            index += 1
        
        # If there are remaining negative numbers, append them
        while j < len(negative):
            arr[index] = negative[j]
            j += 1
            index += 1
