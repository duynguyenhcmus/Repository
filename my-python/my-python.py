print("Hello world")
import numpy as np
number_of_steps=1000
walks=np.random.randint(0,2,size=number_of_steps)
position=0
value=[]
for i in range(number_of_steps):
    if walks[i]==0:
        position+=-1
        value.append(position)
    else:
        position+=1
        value.append(position)
value
