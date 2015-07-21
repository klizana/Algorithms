# klizana
# Merge Sort 2015
# Running time: O(nlog(n))

def merge_sort(a):	
	n = len(a)
	
	if n == 1 :
		return a
	
	l1 = a[:len(a)/2]
	l2 = a[len(a)/2:]
	
	#recursive calls
	l1 = merge_sort(l1)
	l2 = merge_sort(l2)

	return merge(l1,l2)

def merge(b,c):
    d =[]
    while (len(b) > 0 and len(c) > 0):
        if b[0] > c[0]:
            d.append(c.pop(0))
        else:
            d.append(b.pop(0))
    
    while len(b) > 0:
        d.append(b.pop(0))
    while len(c) > 0:
        d.append(c.pop(0))
    
    return d;
            
if __name__ == '__main__':
    # main
    print "Enter the numbers in the array separated by comma:"
    a = []
    arrayIn = raw_input()
    a = arrayIn.split(',')
    print "Array to sort: "	
    print a
    print "Sorted Array: "
    print merge_sort(a)
