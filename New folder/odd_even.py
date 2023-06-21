def find_even(a,b):
    sum=0
    odd=0
    for i in range(a,b):
        if i%2==0:
            sum=sum+i
        print("sum is ",sum)
        if i%2!=0:
            odd=odd+i
        print("sum of odd is",odd)
find_even(1,51)