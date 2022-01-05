#ceiling of a target in an array of number
# ceil = smallest element in an array greater or equal to target
def ceiling(arr,target):
    start = 0
    end = len(arr)-1
   # if target>arr[len(arr)-1]: # this is the case when the target is greater than the last number so we cant find the ceil
    #    print("There is no ceiling")  
    while start<=end:
        mid = start + (end-start)//2
        if arr[mid] == target:
            print(arr[mid])       # if our target is equal to mid we have to print
            break
        elif arr[mid]<target:
            start = mid+1
        elif arr[mid]>target:
            end = mid-1
    if start>end:
         print(arr[start])  # when while fails we will have    end  target   start 
                                                    # so the greatest number of target (ceil ) is start 
arr = [2,3,6,8,10,16]
ceiling(arr,8)