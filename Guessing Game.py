
# coding: utf-8

# In[2]:

import sys
inputstatement = sys.stdin.readline()
This is a worderful 
inputstatement


# In[1]:

import random
com_num=random.randint(0,100)
low=0
high=100
while True:
    use_num = int(input("Enter the number between 0-100:"))
    if use_num>100:
        print("Wrong Entry Please Check the range of Number")
    elif use_num<0:
        print("Wrong Entry Please Check the range of Number")
    elif use_num>com_num:
        print("Guess Lower between ",low,"&",use_num)
        high=use_num
    elif use_num<com_num:
        print("Guess Higher between",use_num,"&",high)
        low=use_num
    else:
        print("Congrats You have Gussed The Correct Number")
        break


# In[ ]:




# In[ ]:



