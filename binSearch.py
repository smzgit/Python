def binSearch(arr,left,right,key):
	if left>right:
		return -1
	mid = (left+right)//2
	if arr[mid]==key:
		return mid
	if key<arr[mid]:
		return binSearch(arr,left,mid-1,key)
	return binSearch(arr,mid+1,right,key)





arr=[12,33,44,66,72,89,90,110]
key = 414
fg = binSearch(arr,0,len(arr)-1,key)
if fg==-1:
  print('element not found')
else:
	print('elemt found at ',fg)
