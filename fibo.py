'''
Euler second python
'''

import numpy as np
fibo=[1,2]
oushu=[2]
for i in range(0,5000000): 
        x=fibo[i]+fibo[i+1]
        if x<4000000:
                fibo.append(x)
                if x%2==0:
                        oushu.append(x)
        else :
                break
np_oushu=np.array(oushu)
sum=np.sum(np_oushu)
print(sum)  

