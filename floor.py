# floor = greatest number which is smaller or equal to target 
def floor(arr,target):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = start + (end-start)//2
        if arr[mid]==target:
            print(arr[mid])     # when its is equal we will print it 
            break
        elif arr[mid]<target:
            start = mid+1
        elif arr[mid]>target:
            end = mid-1
    if start>end:     # when while loop breaks then the condintion becoms end target start
        print(arr[end])                                                      # now we can observe that lesser number to target is end so we will print end
arr = [1,2,5,8,9,12,18]
floor(arr,7)