List=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144] #an example list

def mean(List):
	'''
    Sum a list and divide by its length to get the mean
    '''
	tot=0.0 #A variable to hold the total
	count=0.0 #A variable to increment and ultimately divide by
	for i in List:
		tot=tot+i #increment the total by an element in the list
		count=count+1 #increment the count by 1
	return tot/count #return the mean
print 'This is the mean:', mean(List) #run the function, printing off the list

def binary_search(find_this,list,left,right):
	'''
    Go through a sorted list, and find the position of a specific value, recursively dividing the list in half
    '''
	if left>right: #if there's an error in the input, return -1
		return -1
	mid=(left+right)/2 #Get the midpoint of the list
	if list[mid]==find_this: #The base case; if the middle is found, end the recursion and return mid
		return mid
	elif list[mid]>find_this: #Continue searching in the left side of the list if mid is too high; use a recursive call
		return binary_search(find_this,list,left,mid-1)
	elif list[mid]<find_this:#Continue searching in the righ side of the list if mid is too low; use a recursive call
		return binary_search(find_this,list,mid+1,right)

print(binary_search(55,List,0,len(List)-1)) #run the binary_search function