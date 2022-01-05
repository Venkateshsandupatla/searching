# Given a positive integers N, the task is to find the smallest number whose sum of digits is N.

# https://www.geeksforgeeks.org/find-the-smallest-number-whose-sum-of-digits-is-n/
def sum(N)->int:
        sum1 = 0
        while (N!=0):
             r = N%10
             sum1 = sum1+r
             N = N // 10 
        
        return sum1
def smallestnumber(N)->int:
    i = 1
    while (1):
        if(sum(i)==N):
            print(i)
            return i
     
        i+=1

N = int(input())

smallestnumber(N)


 