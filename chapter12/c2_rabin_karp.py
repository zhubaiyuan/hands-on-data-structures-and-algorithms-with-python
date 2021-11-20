
def generate_hash(text, pattern):
    # stores unicode value of each character in text
    ord_text = [ord(i) for i in text]
    # stores unicode value of each character in pattern
    ord_pattern = [ord(j) for j in pattern]
    # stores length of the text
    len_text = len(text)
    # stores length of the pattern
    len_pattern = len(pattern)
    # stores the length of new array that will contain the hash values of text
    len_hash_array = len_text - len_pattern + 1
    # Initialize all the values in the array to 0.
    hash_text = [0]*(len_hash_array)
    hash_pattern = sum(ord_pattern)
    # step size of the loop will be the size of the pattern
    for i in range(0, len_hash_array):
        if i == 0:                                                 # Base condition
            # initial value of hash function
            hash_text[i] = sum(ord_text[:len_pattern])
        else:
            # calculating next hash value using previous value
            hash_text[i] = ((hash_text[i-1] - ord_text[i-1]) +
                            ord_text[i+len_pattern-1])
    # return the hash values
    return [hash_text, hash_pattern]


def Rabin_Karp_Matcher(text, pattern):
    # convert text into string format
    text = str(text)
    # convert pattern into string format
    pattern = str(pattern)
    # generate hash values using generate_hash function
    hash_text, hash_pattern = generate_hash(text, pattern)
    # length of text
    len_text = len(text)
    # length of pattern
    len_pattern = len(pattern)
    # checks if pattern is present atleast once or not at all
    flag = False
    for i in range(len(hash_text)):
        # if the hash value matches
        if hash_text[i] == hash_pattern:
            # count stores the total characters upto which both are similar
            count = 0
            for j in range(len_pattern):
                # checking equality for each character
                if pattern[j] == text[i+j]:
                    # if value is equal, then update the count value
                    count += 1
                else:
                    break
            # if count is equal to length of pattern, it means match has been found
            if count == len_pattern:
                flag = True                                          # update flag accordingly
                print('Pattern occours at index', i)
    # if pattern doesn't match even once, then this if statement is executed
    if not flag:
        print('Pattern is not at all present in the text')


Rabin_Karp_Matcher("101110000011010010101101", "10112")

# Works for numeric
Rabin_Karp_Matcher("101110000011010010101101", "1011")

# Works for alphabets
Rabin_Karp_Matcher("ABBACCADABBACCEDF", "ACCE")

# Works for alpha numeric
Rabin_Karp_Matcher(
    "abc1-3klm890zsdoifjwej8cjv09wn vn09aej09jv 09wje09cj 09 j093j0 9j 092j3 09c09", "09w")
