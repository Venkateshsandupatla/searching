def Binary_search(array, value):
    array = sorted(array)
    start = 0
    end = len(array)-1
    middle = int((start+end)/2)
    while not array[middle] == value:
        if array[middle] > value:
            print("we will have number at left side")
            end = middle-1
            middle = int((start+end)/2)
        elif array[middle] < value:
            print("we will have number at right side")
            start = middle+1
            middle = int((start+end)/2)

    print("We found the number at {}".format(middle))


arr = [2, 3, 1, 5, 4, 7, 6, 8]
Binary_search(arr, 1)
