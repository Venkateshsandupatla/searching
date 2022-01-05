# https://leetcode.com/problems/search-in-rotated-sorted-array/
def search(nums,target)->int:
        def pivot(nums)->int:
            start = 0 
            end = len(nums)-1
            while start<end:
                mid = start + (end-start)//2
                if (mid<end and nums[mid]>nums[mid+1]):
                    return mid
                elif (mid>start and nums[mid]<nums[mid-1]):
                    return mid-1
                elif nums[start]<nums[mid]:
                    start = mid+1
                elif nums[start]>=nums[mid]:
                    end = mid-1
            return start
        def searchleft(nums,target,pivot)->int:
            start = 0
            end = pivot
            while start<=end:
                mid = start + (end-start)//2
                if nums[mid]<target:
                    start = mid+1
                elif nums[mid]> target:
                    end = mid-1
                else:
                    return mid
            return -1
        
        def searchright(nums,target,pivot)->int:
            start = pivot + 1
            end = len(nums)-1
            while start <=end:
                mid = start + (end-start)//2
                if nums[mid]<target:
                    start = mid +1
                elif nums[mid]>target:
                    end = mid-1
                else:
                    return mid
            return -1
        
        pivot = pivot(nums)
        if nums[pivot] == target:
            print(pivot)
            return pivot
    #    elif searchleft(nums,target,peak)!=-1:
    #        ans = searchleft(nums,target,peak)
    #    elif searchright(nums,target,peak)!=-1:
    #        ans = searchright(nums,target,peak)
        else:
            ans = searchleft(nums,target,pivot)
            if ans == -1:
                 ans = searchright(nums,target,pivot)

        print(ans)
        return ans

arr = [4,5,6,7,0,1,2]
#arr = [5,1,3]
arr = [1,3]
search(arr,0)
        