class Solution:
    
    # Function to reverse words in a given string.
    def reverseWords(self, s):
        # Step 1: Split the string into words using dot ('.') as delimiter
        words = s.split('.')
        
        # Step 2: Reverse the list of words
        words.reverse()
        
        # Step 3: Join the words back using dot ('.') and return
        return '.'.join(words)