n=int(input("ENTER NUMBER OF N TERMS: "))
if n<=0:
    print("Fibonacci series upto",n,"is not defined")
else:
    first=0
    second=1
    print("The first",n,"numbers in the Fibonacci series= ")
    print(first,",",second,end=",")
    for i in range(2,n):
        fib=first+second
        first=second
        second=fib
        #if fib>n:
            #break
        if i==n-1:
            print(fib,end="")
        else:
            print(fib,end=",")
