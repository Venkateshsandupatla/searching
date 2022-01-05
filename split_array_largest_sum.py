def split_array(arr,m)->int:
    start = 0
    end = 0
    # we know that if we want to create a subarray which has maximum sub that subarray should be the orginal array 
    # so the end or max value is sum of all in array
    # the min value that means we have to create len(array) subarrays and the max value of it is min
    for i in arr:
        end+=i
        start = max(start,i)
    # examle = [7,2,5,10,8]
    # now start became 10 which is max element if the array
    #end became sum of all the elements in the array -> 32
    # that means our answer lies in between 10 and 32 so lets we have to do binary search
    while start<end:
        mid = start + (end-start)//2
        # this mid we will think as potential answer 
        sum = 0
        # the nuumber of pieces or subarrays we can make min is 1 that is the orginal array
        pieces = 1
        for num in arr:
            if sum+num>mid:
                #that means we cananot add one more element in this subarray , i.e, we have created one piece  
                pieces+=1
                #that means the next subarray first element is this number which is also the intial sum of next subarray
                sum = num
            else:
                #this means (sum+num<mid) which means we can element in the subarray
                #so we are adding element we have to add it to sum 
                sum+=num
        #now we have created pieces we have to check it with given m (condition pieces) 
        if (pieces<=m):
            #if pieces are lesser or equal to m that means potential answer(mid) is greater than our orginal answer 
            # so we have to go for left and do binary search 
            end = mid
        elif(pieces>m):
            #pieces are greater than m that means potential answer is lesser than orginal answer
            # so we have to go for right side and do binary search
            start = mid+1
        # at laste when start and end are equal our potential answer that is mid is orginal answer 
        # it passes all the above checks so we have to return the start or end which are equal even the mid to
    return start
arr = [7,2,5,10,8]
split_array(arr,2)