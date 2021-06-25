# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:20:27 2021

@author: snakk
"""

def IsGreaterOrEqual(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

#Leading zeros don't work only in the case of int. So, writing str(0394) gives error
#for leading zeros. But we can write it as string. i.e: int("0394") outputs 394

def largest_number(a):
    a= sorted(a, reverse=True)
    #res=""
    c=0
    while True:
        c=0
        for i in range(len(a)-1):
            if IsGreaterOrEqual(a[i],a[i+1])==0:
                c+=1
                idx=i
                #print(idx,c)
                break
        if c==0:
            break                
        temp= a[idx]
        a[idx]= a[idx+1]
        a[idx+1]= temp
        #print(a)
        
    
# =============================================================================
#     for nums in a:
#         res+=str(nums)         #Doing this and returning res will return the answer as a concatenated string of that list
#     return res
# =============================================================================
    return a

def largest_numbercopied(lst):
    answer = []
    while lst!=[]:
        max_digit = 0
        for digit in lst:
            if IsGreaterOrEqual(digit, max_digit):
                max_digit = digit
                #print(max_digit)
        answer.append(max_digit)
        #print(answer)
        lst.remove(max_digit)
    
    return answer


def stresstest():
    import random
    okcounter=0
    while True:
        n=random.randint(1,100)
        a=[]
        for i in range(n):
            a.append(random.randint(1,1000))
        
        print(f'numbers= {a}\n')
        print(f'Result1= {largest_number(a)}\n')
        print(f'Result2= {largest_numbercopied(a)}')
        
        if largest_number(a)==largest_numbercopied(a):
            okcounter= okcounter+1
            print('ok\n')
            if okcounter>=100:
                break

        else: 
            print('Error')
            break

#print(largest_numbercopied([394, 71, 40, 792, 517]))
stresstest()

def timecounter(func1, func2, number):
    from timeit import timeit
    import random
    n=random.randint(1,100)
    a=[]
    for i in range(n):
        a.append(random.randint(1,1000))
            
    time1= timeit(lambda: largest_number(a), number= number)
    time2= timeit(lambda: largest_numbercopied(a), number=number)

    time= {"Time1": round(time1,4),"Time2": round(time2,4)}
    
    min= "Time1"
    for key in time:
        if time[key]<time[min]:
            min= key
    
    for key in time:
        if time[key]==time[min]:
            print(f'The fastest is {key}!\n')
        
    return time


print(timecounter(largest_number, largest_numbercopied, number= 1000))
n= int(input("Input the size of the list:\n"))
print("Input the list:")
a=[]
for i in range(n):
    a.append(int(input()))
print("result1="+str(''.join([str(i) for i in largest_number(a)])))
print("result2="+str(''.join([str(i) for i in largest_numbercopied(a)])))