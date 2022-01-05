#https://www.geeksforgeeks.org/minimum-characters-required-to-be-removed-to-make-frequency-of-each-character-unique/
# write a function solution that given a string S consisting of N  characters , returns the minimum number 
# of letters that must be deleted to obtain an even word 
#Examples :
# Given S = 'acbcbba' -> here a is 2 , b is 3 , c is 2 --> here a is 2 , bis 3 so we have to delete 1 b from b so that our string will become even string 
def solution(S):
    N = len(S)
    mp = {}
    count = 0
    for i in range(N):
        mp[S[i]] = mp.get(S[i],0)+1
    for it in mp:
        if(mp[it]%2 !=0):
            count+=1
    print(count)
    #return count

s = input()
solution(s)
