#wap to show multiplication table of first 20 prime number using nested for loop

def check_prime(num):
    if num<2:
        return 0
    for i in range(2,int(num/2)+1):
        if num%i==0:
            return False
    return True

count=0
number=1
prime_list=[]
while count<20:
    if check_prime(number):
        prime_list.append(number)
        count+=1
    number+=1

print(prime_list)
for i in prime_list:
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    print("\t")
    
``
        



    

            
      
        