def brute_force(text, pattern):
    # The text which is to be checked for the existence of the pattern
    l1 = len(text)
    l2 = len(pattern)   # The pattern to be determined in the text
    i = 0
    j = 0
 # looping variables are set to 0

    flag = False        # If the pattern doesn't appear at all, then set this to false and execute the last if statement
    while i < l1:       # iterating from the 0th index of text
        j = 0
        count = 0       # Count stores the length upto which the pattern and the text have matched
        while j < l2:
            # statement to check if a match has occoured or not
            if i+j < l1 and text[i+j] == pattern[j]:
                # if the statement evaluates to true, then update count
                count += 1
            j += 1
        if count == l2:                             # if total number of successful matches is equal to count of the array
            # print the starting index of the successful match
            print("\nPattern occours at index", i)
            # Even if the matching occours once, set this flag to True
            flag = True
        i += 1
    # If the pattern doesn't occours even once, this statement gets executed
    if not flag:
        print('\nPattern is not at all present in the array')


brute_force('acbcabccababcaacbcaabacbbc',
            'acbcaa')                    # function call
