
# Done using extra data structure 
def unique_chars( str ): 
    buckets = [0] * 256
    for c in str:
        if buckets[ord(c)] == 1:
            return False
        buckets[ord(c)] = buckets[ord(c)] + 1
    return True

#Using no extra data structures
def unique_chars2( str ):
    sorted_str = sorted(str)
    for i in range(0,len(str) - 1):
        if sorted_str[i] == sorted_str[i+1]:
            return False
    return True

while (1):
    str = raw_input("Enter a string: ")
    is_unique = unique_chars2( str )
    if is_unique :
        print("There were unique characters")
    else :
        print("There were some non-unique characters")



