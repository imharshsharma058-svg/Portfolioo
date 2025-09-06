print("enter your subject marks ")
m = int (input("first subject number"))
p  = int (input("second subject number"))
s = int (input("third subject number"))

avg = (m+p+s)/3
print(avg)
if(avg>=80):
    print("getting A rank")
elif(avg>=60):
    print("getting B rank")
elif(avg>=40):
    print("getting c rank")
elif(avg>=20):
    print("getting D rank")
else:
    print("better luck next time")