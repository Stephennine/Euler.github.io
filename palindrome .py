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


palindrome(100,1000)        
difference(100)      

