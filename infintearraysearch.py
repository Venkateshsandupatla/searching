# assume we have a infinte array and we have to find the index of a particular element
# first thing is we have to apply the binary search because we have sorted array
#but the problem here is we dont have the length of array whcih we consider it as the end in our binary search
#So first we have to find the start and end where our target lies then we have to apply binary search

def searchinginfinitearray(nums:list[int],target:int)->int:
    
    start = 0  # fiirst we assumed the start is 0 and end is 1
    end = start+1
    def range(nums,target,start,end)->int:  # this function gives the range where our target lies 
                                            # it gives the start and end of the binary search                    
        while target>nums[end]:             # we know that if pur target is more than end that means we have target at regith side of present end
                                            # now new start = end +1 -> 0+1 =1
            newstart = end+1                # in bseacrh we go by n/2 every time now we have to find s,end so we go reverse 
            end = end+(end-start+1)*2       # that is every time we increase our array by twice as previous aaray and find the start and end
            start = newstart            # end becomes end + (e-s+1)*2 ->1+(1-0+1)*2=5 now from 1,5 we have 4 in previous 0,1 we have two like this every time we double the array
        return start,end
    start ,end = range(nums,target,start,end) # now we got the start and end now its a simple binaryy search of element

    def answer(nums,target,start,end)->int:
        while start<=end:
            mid = start + (end-start)//2
            
            if nums[mid]<target:
                start = mid+1
            elif nums[mid]>target:
                end = mid-1
            else:
                print(mid)
                return mid
        return -1 # if the loop break that means the number doesnt exist but it wont happen 
    answer(nums,target,start,end)
arr = [2,3,5,6,7,8,9,10,11,14,16,18,19,20,25,30,34,38,40]
searchinginfinitearray(arr,16)