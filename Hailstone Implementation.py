

def hailstorm(x):
    count=0
    while x!=1:
        if x%2==0:
            x = x//2
            count+=1          
        else:
            x=(3*x)+1
            count+=1
    print(count)
for i in range(2,100):
    hailstorm(i)
get_ipython().run_line_magic('timeit', 'hailstorm')

