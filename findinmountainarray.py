#Question:  https://leetcode.com/problems/find-in-mountain-array/

#step 1 we have to find the peak 
#step 2 if the peak is equal to our target just return it
#step 3 if not search left side of peak by binary search
#step4 if not found search right side of peak using binary search

def peak(mountain_arr:'MountainArray')->int:
            start = 0
            end = len(mountain_arr)-1
            while start<end:
                mid = start + (end-start)//2
                if mountain_arr[mid]>mountain_arr[mid+1]:
                    end = mid
                elif mountain_arr[mid]<mountain_arr[mid+1]:
                    start = mid+1
            return start

        
        
def SearchLeft(mountain_arr:'MountainArray',target,end)->int:
            start = 0
            end = end
            while start<=end:
                mid = start + (end-start)//2
                if mountain_arr[mid] == target:
                    return mid
                elif mountain_arr[mid]<target:
                    start = mid+1
                elif mountain_arr[mid]>target:
                    end = mid-1
            return -1

def SearchRight(mountain_arr:'MountainArray',target,start)->int:
            start = start+1
            end = len(mountain_arr)-1
            while start<=end:
                mid = start + (end-start)//2
                if mountain_arr[mid] == target:
                    return mid
                elif mountain_arr[mid]<target:
                    end = mid-1
                elif mountain_arr[mid]>target:
                    start = mid+1
            return -1
            
def result(mountain_arr,target,peak)->int:
    if mountain_arr[peak]==target:
                ans=peak
    elif SearchLeft(mountain_arr,target,peak) != -1:
                ans=SearchLeft(mountain_arr,target,peak) 
    else:    
                ans=SearchRight(mountain_arr,target,peak)  
            
    print(ans)
    return ans

mountain_arr=[1,2,3,5,3]
peak = peak(mountain_arr)
result(mountain_arr,0,peak)
