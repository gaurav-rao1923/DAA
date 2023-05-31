print("Create an array")
array=[]
for i in range(0,5):
     array.append(input("Enter elements :"))
b=int(input("Enter the index of the elements you wish to :"))
for i in range (0,5):
     if i==b:
        print(array[i])
