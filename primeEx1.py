n=int(input("enter a number:"))
z=0
for i in range(1,n+1):
    if n%i==0:
        z=z+1
if z==2:
        print("prime")
else:
    print("not prime")
