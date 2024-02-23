def arms(n):
    n3=str(n)
    n4=len(n3)
    n1=n
    n2=0
    while (n>0):
        rem=n%10
        n2=n2+rem**n4
        n=n//10;

    if (n1==n2):
        print(f"{n1} is an armstrong number")
    else:
        print(f"{n1} is not an armstrong number")

a=10
arms(a)
x=set('abc')
x.add('san')
x.update(set(['p','q']))
print(x)
