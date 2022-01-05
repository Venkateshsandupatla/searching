def smallest(int,arr)->int:
    arr = sorted(arr)
    count = 1
    i =0
    while arr[i] == arr[i+1]:
        count+=1
        i+=1
    return count
    
n=int(input("Number of elements in the array:-"))
arr=list(map(int, input("elements of array:-").strip().split()))
smallest(n,arr)
