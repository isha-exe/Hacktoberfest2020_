arr=[0,1,2,3,4]
print('List has the items:',arr)
low=0
high=len(arr)                               #finding length of the array
num=int(input("Enter element to be searched"))
while low<=high:
    mid=int((low+high)/2)                  #finding middle most element of the array
    if num==arr[mid]:                      #if the number is equal to middle most element print the element and get out of the loop(break)
        print("Num is present at index ",mid)
        break
    elif  arr[mid]<num:
        low=mid+1                           #if the number is greater than the middle number increase low
    else:
        high=mid-1                          #else if the number is smaller than the middle number decrease high
