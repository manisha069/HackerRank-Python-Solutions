def count_substring(string, sub_string):
    size = len(string)
    siz2= len(sub_string)
    c=0
    for i in range(size-2):
        y = string[i:i+siz2]
        if y == sub_string:
            c += 1
    return c
    
