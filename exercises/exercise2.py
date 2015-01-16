L=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

tot=0.0
count=0.0
for i in L:
	tot=tot+i
	count=count+1
mean=tot/count
print 'This is the mean:', mean

x=55

def binary_search(x,list,left,right):
	if left>right:
		return -1
	mid=(left+right)/2
	if L[mid]==x:
		return mid
	elif L[mid]>x:
		return binary_search(x,list,left,mid-1)
	elif L[mid]<x:
		return binary_search(x,list,mid+1,right)

print(binary_search(x,list,0,len(L)-1))