arr = [47,2,3,12,9,50,31,100,200,10,21,90,14]
#arr = [6,5,3,2,4,7,8,9]

def quicksort(src, s, e) :
    if s >= e :
        return

    std = src[s]
    i = s
    j = e
    while i < j :

        while i < j and src[j] >= std:
            j -= 1

        if i < j :
            src[i] = src[j]
            i += 1

        while i < j and src[i] <= std:
            i += 1

        if i < j:
            src[j] = src[i]
            j -= 1

    src[i] = std
    print arr, s, e

    quicksort(src, s, i - 1)
    quicksort(src, i + 1, e)

quicksort(arr, 0, len(arr)-1)
print arr