print("GCD of the given number is :")
m=int(input("Please enter the value for m :"))
n=int(input("please enter the value for n :"))
while(n!=0):
    r=m%n
    m=n
    n=r

print(m)
