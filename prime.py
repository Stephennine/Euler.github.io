x=600851475143
prime=[]
a=1
while a==1:
    for i in range(3,600851475143 ,2):
        if x%i==0:
            x=x/i
            prime.append(i)
            print(i)
            break
        if i>=100000:
            a=0
            break
