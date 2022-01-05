cars = [2,3,42,14,5,1,5,6,67]
lengt = len(cars)
#print(lengt)
def car(car_parking,mycar_number,n):
 mycar = mycar_number
 for i in range(0,n):
    if car_parking[i]  == mycar:
        print("my car is found at {} position".format(i))
        break
# else:
 # print("Your car is not found")


car(cars,4,lengt)
