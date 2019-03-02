#!/usr/bin/env python3
# encoding: utf-8

## 注意：题目中是第二公共单词,我暂且理解为第二长个.
##首先把两个字符串分别按照空格分割,由于使用字典需要构造,那么用列表来代替吧
##时间复杂度为:分割两个字符串2*o(n),判断字符串是否存在,最差o(n^2),最后把列表中的
##字符串按照长度进行排序o(n^2),加一块总体时间为:n^2
#引用了一个新的列表,空间复杂度o(n),一共为o(n)
def insert_sort(myList):
    for i in range(1,len(myList)):
        #要排序的牌
        key = myList[i]
        #手中右边的牌
        j = i - 1
        #与 手中的牌逐一比较
        while j >= 0 and len(myList[j]) < len(key):
            #满足条件时,交换两张牌的顺序
            myList[j+1] = myList[j]
            j -= 1
        myList[j+1] = key

def exam1(str1,str2):
    #分割
    str1_list = str1.split(" ")
    str2_list = str2.split(" ")
    #判断公共字符串
    com_list = [x for x in str1_list if x in str2_list]
    insert_sort(com_list)
    if len(com_list) > 1:
        return com_list[1]
    elif len(com_list) == 1:
        return com_list[0]
    else:
        return "NULL"

###由于是连续正整数,因此满足等差数列,因为是连续的使用区间加法可以得到总和
###有一个奇数就可以满足条件
###时间复杂度是O(n),空间复杂度o(1)
###sum(i,j) = number
def exam2(number):
    if number < 2:
        print("NONE")
        return 
    if (number & (number-1)) == 0: #是2的平方,直接返回
        print("NONE")
        return
    def add(m,n):
        sm = 0
        for i in range(m,n+1):
            sm += i
        return sm
    i = 1
    j = 2 #从最小数开始循环
    while i <= number/2: #最大循环一半
        msum = add(i,j)
        while msum!=number:
            if msum>number:
                i+=1
            else:
                j+=1
            if i >= number /2:
                break
            msum = add(i,j) #直到循环的相等了
        if msum == number:
            print([p for p in range(i,j+1)])
        i += 1

if __name__ == '__main__':
    print(exam1("This is C programming text","This is a text for C programming"))
    exam2(15)
