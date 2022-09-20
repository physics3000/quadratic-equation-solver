#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

repeat= 'yes' 

#allows to equation to be solved repeatdly

while(repeat=='yes'):

    a= float(input ('input the coefficent of x squared'))

    b= float(input ('input the coefficent of x'))

    c=float(input('input the constant term'))

#the discriminant

    discriminant= b**2-4*a*c

    if discriminant>0:

#the first root

        root_1=(-b + math.sqrt(b**2-4*a*c))/(2*a)

#the second root

        root_2=(-b - math.sqrt(b**2-4*a*c))/(2*a)

        print('the first solution is x=',root_1)

        print('the second solution is x=', root_2)
    
    else:
        print('the equation has no real solutions')

    repeat= input('do you want to solve another (yes or no)?')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




