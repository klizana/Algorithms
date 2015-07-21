# klizana
# counting_inversions.py
#
# Problem 
# Input : array A[] containing the numbers 1,2,3,..,n in some arbitrary order
# Output : number of inversions = number of pairs (i,j) of array indices with i<j and A[i] > A[j]
# Running time: O(nlog(n))

def sort_and_count(a):
    l =len(a)
    
    if l == 1:
        return (a, 0)

    sort_b = a[:l/2]
    sort_c = a[l/2:]
    
    (sort_b, count_b) = sort_and_count(sort_b)   
    (sort_c, count_c) = sort_and_count(sort_c)
    
    (sort_d, count_d) = count_split_inv(sort_b, sort_c, l)
    
    total_inv = count_b + count_c + count_d

    return (sort_d, total_inv)
      
def count_split_inv(b,c,n):
    
    inv=0
    d = []
    
    while  (len(b) > 0 and len(c) > 0):
        if b[0] < c[0]:
            d.append(b.pop(0))
        else:
            d.append(c.pop(0))
            inv = inv + len(b)

    # border case: only have elements in array b 
    while (len(b) > 0):
            d.append(b.pop(0))

    # border case: only have elements in array c 
    while (len(c) > 0):
            d.append(c.pop(0))

    return (d, inv)

if __name__ == '__main__':

    # main
    a = []
    sorted_a = []
    
    print "Enter the numbers in the array separated by comma:"
    
    arrayIn = raw_input()
    a = arrayIn.split(',')    
    
    (sorted_a, inv) = sort_and_count(a)
    
    print "Sorted Array: "
    print sorted_a
    print "inversions: "
    print inv

