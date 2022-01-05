def searchingrange(nums, target)->list[int]:
    def search(nums,target,firstindex:bool)->int:
        ans = -1
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]<target:
                start = mid+1
            elif nums[mid]>target:
                end = mid-1
            else:
                ans = mid
                if firstindex:
                    end = mid-1
                else:
                    start = mid+1
        return ans
    first = search(nums,target,firstindex=True)
    ending = search(nums,target,firstindex=False)
    ans = [first,ending]
    print(ans)
    return ans    


nums = [5,6,7,7,7,8,8,9]
searchingrange(nums,7)