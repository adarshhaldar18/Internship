#!/usr/bin/env python
# coding: utf-8

# # Q11.Write a python program to find the factorial of a number. 

# In[20]:


# To take input from the user
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)


# # Q12.Write a python program to find whether a number is prime or composite

# In[23]:


# To take input from the user
num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither prime NOR composite number")
else:
    print(num, "is NOT a prime number it is a COMPOSITE number")


# # Q13.Write a python program to check whether a given string is palindrome or not.

# In[24]:


# To take input from the user
my_string=input("Enter string:")
if(my_string==my_string[::-1]):
    print("The string is a palindrome")
else:
    print("The string isn't a palindrome")


# 
# # Q14.Write a Python program to get the third side of right-angled triangle from two given sides. 

# In[25]:


#Lets make a function which will give our any value of right angled triangle when we give 2 side's value and third side as x
def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "You know the answer!"
    
print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))


# # Q15.Write a python program to print the frequency of each of the characters present in a given string.

# In[29]:


# initializing string
test_str = "IamADatarainedStudent"
 

# of each element in string
all_freq = {}
 
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
 

print("Count of all characters in GeeksforGeeks is :\n "
      + str(all_freq))


# In[ ]:




