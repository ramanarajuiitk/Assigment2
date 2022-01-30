##Create the below pattern using nested for loop in Python.
##  *
##  * *
##  * * *
##  * *
##  *
n=int(input('enter number'))
for i in range(n+1):
    if(i<n):
        for j in range(i):
            print('*',end='')
    else:
        for j in range(n):
            for k in range(n-j):
                 print('*',end='')
            print('')
    print('')    
##Write a Python program to reverse a word after accepting the input from the user.
string1=input('enter a word')
print(string1[::-1])