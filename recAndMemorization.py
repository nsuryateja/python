import time 
def withRecursion(n):
    if n==1 or n==2:
        return 1
    else:

        return withRecursion(n-1)+withRecursion(n-2)
startTime = time.time()
print(withRecursion(35))
print('Time taken by recursion: ' + str(round(time.time()-startTime)))
search_me = {}
def withMem(n):
    if n in search_me.keys():
        return search_me[n]
    elif n==1 or n==2:
        return 1
    else:
        val = withMem(n-1)+withMem(n-2)
        return val
    search_me[n]=val
startTime = time.time()
print(withMem(35))
print('Time taken by memorization: ' + str(round(time.time()-startTime)))
