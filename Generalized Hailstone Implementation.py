#!/usr/bin/env python
# coding: utf-8

# In[21]:


def hailstone(x):
    count1=0
    for a in range(1,11):
        for b in range(1,11):
            mylist=[]
            y=x
            #print(f'Pair under consideration:({a},{b})')
            oddcount=0
            while (y>0):
                if oddcount<=100:
                    if y%2==0:
                        y = y//2
                        if y in mylist:
                            count1=count1+1
                            break
                        else:
                            mylist.append(y)
                           
                    else:
                        oddcount=oddcount+1
                        y=(a*y)+b
                        if y in mylist:
                            count1=count1+1
                            break
                        else:
                            mylist.append(y)
                else:
                    #print("Zero convergence on this pair")
                    break      
                    
    #print(f'The total count of holding patterns for {x} with a and b taking values 1 to 10 is {count1}')
    return count1
x=0
m=1000
for i in range(1,m+1):
    x=x+hailstone(i)
print(f'The total count of holding patterns for numbers 1 to {m} with a and b in range of 1 to 10 is {x}')
#The Print statement output takes approx 10-15seconds to display out put for range 1-1000

