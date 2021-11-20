
def pfun(pattern):          # function to generate prefix function for the given pattern
    n = len(pattern)        # length of the pattern
    prefix_fun = [0]*(n)    # initialize all elements of the list to 0
    k = 0
    for q in range(2, n):
        while k > 0 and pattern[k+1] != pattern[q]:
            k = prefix_fun[k]
        # If the kth element of the pattern is equal to the qth element
        if pattern[k+1] == pattern[q]:
            k += 1                          # update k accordingly
        prefix_fun[q] = k
    return prefix_fun                       # return the prefix function


def KMP_Matcher(text, pattern):              # KMP matcher function
    m = len(text)
    n = len(pattern)
    flag = False
    # append dummy character to make it 1-based indexing
    text = '-' + text
    pattern = '-' + pattern                 # append dummy character to the pattern also
    # generate prefix function for the pattern
    prefix_fun = pfun(pattern)
    q = 0
    for i in range(1, m+1):
        # while pattern and text are not equal, decrement the value of q if it is > 0
        while q > 0 and pattern[q+1] != text[i]:
            q = prefix_fun[q]
        # if pattern and text are equal, update value of q
        if pattern[q+1] == text[i]:
            q += 1
        # if q is equal to the length of the pattern, it means that the pattern has been found.
        if q == n:
            # print the index, where first match occours.
            print("Pattern occours with shift", i-n)
            flag = True
            q = prefix_fun[q]
    if not flag:
        print('\nNo match found')


# function call, with two parameters,text and pattern
KMP_Matcher('aabaacaadaabaaba', 'aabac')
