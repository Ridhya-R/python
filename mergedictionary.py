mydict1={}
print("Enter elements of first dictionary ")
while True:
    key=input("Enter a key (or q to quit): ")
    if key=='q':
        break
    value=int(input("enter a value: "))
    mydict1[key]=value
print("Enter elements of second dictionary ")
mydict2={}
while True:
    key=input("Enter a key(or q to quit): ")
    if key=='q':
        break
    value=int(input("Enter a value: "))
    mydict2[key]=value
print(mydict1|mydict2)
