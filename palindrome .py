import numpy as np
def palindrome(st,last):
    for i in range(int(st),int(last)):
        for j in range(i,int(last)):
            x=i*j
            str_t=str(x)
            t=list(str_t)
            length=len(str_t)
            if length%2==0:
                for y in range(0,int(length/2)):
                    if t[y]!=t[-y-1]:
                        break
                    if y==length/2-1:
                        print(x)
            else:
                for y in range(0,int((length-1)/2)):
                    if t[y]!=t[-y-1]:
                        break
                    if y==(length-1)/2:
                        print(x)
def difference(end):
    b=[]
    c=[]
    for i in range(1,int(end+1)):
        b.append(i*i)
        c.append(i)
    np_b=np.array(b)
    np_c=np.array(c)
    print(sum(np_c)*sum(np_c)-sum(np_b))
def prime_num(x):
    prime=[2,3]
    i=3
    while True:
        i=i+2 
        if i%3==0:
           continue
        k=int(i**0.5)
        if k<5:
            for j in range(3,i,2):
                if i%j==0:
                   break
                if j>=i/2:
                    prime.append(i)
                    break  
        else:
            count=0
            for j in range(5,k+5,2):
                count=count+1
                if count==2:
                    count=0
                    continue
                if i%j==0:
                   break
                if j>=k:
                   if i==25:
                       break
                   prime.append(i)
                   break  
        length=len(prime)
        if length==x:
            print(prime)
            break   
def product():
     last_multiple=[]
     buf=""
     file=open("F:\python\Python_VS\Euler_function\Euler.github.io\j.txt")
     list_arr = file.readlines()
     l = len(list_arr)
     for i in range(l):
        list_arr[i] = list_arr[i].strip()
     for i in range(0,l):
         buf=buf+list_arr[i]  
     list_buf=list(buf)
     lengthlist=len(list_buf)
     for i in range(lengthlist-13):
        multiple=int(list_buf[i])
        for j in range(1,13):
            multiple=int(list_buf[i+j])*multiple
        last_multiple.append(multiple)
     np_last_multiple=np.array(last_multiple)
     print(np.max(np_last_multiple))
def Special_Pythagorean_triplet(sum):
    for  a in range(1,sum):
        for b in range(a,sum):
            c=sum-a-b
            first=a*a+b*b
            second=c*c
            if first==second:
                print(str(a)+"*"+str(b)+"*"+str(c)+"="+str(a*b*c))
                break
def Summation_of_primes(x):
        prime=[2]
        i=3
        while True:
            for j in range(3,i+2,2):
                if j>(int(i/3)+1):
                    prime.append(i)
                    break
                if i%j==0:
                    break
            i=i+2
            if i+2>x:
               np_prime=np.array(prime)
               print(sum(np_prime))
               break
def Grid():
    x=5
    print(x)
#palindrome(100,1000)        
#difference(100)      
#prime_num(10001)
#product()
#Special_Pythagorean_triplet(1000)
#Summation_of_primes(2000000)
Grid()
