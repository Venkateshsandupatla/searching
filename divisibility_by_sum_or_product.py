def numDivisibleBy(arr)->int:
    count = 0
    for i in arr:
        num = i
        sum = 0
        prod = 1
        while i>0:
            
            rem = i%10
            prod = prod*rem
            sum+=rem
            i = i//10
        if  (sum > 0 and num % sum == 0) or (prod > 0 and num % prod == 0):
            count+=1
       
    print(count)


arr = [25,36,45]
numDivisibleBy(arr)    
