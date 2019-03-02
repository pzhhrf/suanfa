
def maxsub(mlist):
    if not mlist:
        return None
    maxv = -10000
    tmpmax = 0
    i = j = 0
    for t,x in enumerate(mlist):
        tmpmax += x
        print(t,i,x,tmpmax,maxv)
        if x > tmpmax:
            i = t
            tmpmax = x
        
        if tmpmax > maxv:
            maxv = tmpmax
            j = t

    return maxv,t,j

def qsort(l,left,right):
    if left < right:
        index = partition(l,left,right)
        qsort(l,0,index)
        qsort(l,index+1,right)


def partition(l,left,right):
    par = l[right-1]
    index = left
    for i in range(left,right):
        if l[i] < par:
            l[index],l[i] = l[i],l[index]
            index+=1
    if l[right-1] < l[index]:
        l[right-1],l[index] = l[index],l[right-1]
    return index

def binSearch(l,k):
    start = 0
    end = len(l) - 1
    rtn = False
    while start <= end:
        index = start + (end-start)//2
        if l[index]>k:
            end = index -1
        elif l[index]<k:
            start = index + 1
        else:
            rtn = True
            break
    print("ss===",rtn)
#[1,3,4,5]
import threading,time
from threading import Thread

number = 1
locka = threading.Lock()
lockb = threading.Lock()

def th1():
    global number
    while number < 30:
        lockb.acquire()
        print("th1===",number)
        number += 1
        locka.release()
        time.sleep(0.5)

def th2():
    global number
    while number < 30:
        locka.acquire()
        print("th2===",number)
        number += 1
        lockb.release()
        time.sleep(0.5)

import asyncio

async def thd1():
    global number
    while number < 30:
        print("th1===",number)
        number += 1
        time.sleep(0.5)
        await asyncio.sleep(0)

async def thd2():
    global number
    while number < 30:
        print("th2===",number)
        number += 1
        time.sleep(0.5)
        await asyncio.sleep(0)

async def test2():
    await asyncio.wait([thd1(), thd2()])

def test():
    t1 = Thread(None,th1)
    t2 = Thread(None,th2)
    locka.acquire()    
    t1.start()
    t2.start()

def reverse(l,k):
    n = len(l)
    k %= n
    l[:] = l[n-k:] + l[:n-k]
    print(l)


def main():
    M = [1,5,3,4,2]
    qsort(M,0,len(M))
    print(M)
    binSearch(M,2)
    # m = [4,-1,2,-2,1,-3,1,-5,4]
    # print(maxsub(m))
    
if __name__ == '__main__':
    # main()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(test2())
    reverse([1,2,3,4,5,6,7],3)
