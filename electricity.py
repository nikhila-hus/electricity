name=input("enter the customer name: ")
units=int(input("enter the units consumed: "))

if units>=1 and units<=100:
    bill=units*2
    print("===electricity bill===")
    print("customer name: ",name)
    print("units consumed: ", units)
    print("Bill amount: ",bill)
elif units >=101 and units<=200:
    bill=units*3
    print("===electricity bill===")
    print("customer name: ",name)
    print("units consumed: ", units)
    print("Bill amount: ",bill)
elif units >=201 and units<=300:
    bill=units*5
    print("===electricity bill===")
    print("customer name: ",name)
    print("units consumed: ", units)
    print("Bill amount: ",bill)
elif units>=301:
    bill=units*7   
    print("===electricity bill===")
    print("customer name: ",name)
    print("units consumed: ", units)
    print("Bill amount: ",bill)
elif units <=0:
    print("invalid units")
else:
    print("unknown error")