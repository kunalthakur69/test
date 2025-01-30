# Code for tower of hanoi by the help of recursion
def tower(n,s,h,d):
    if(n == 0):
        return 1
    tower(n-1,s,d,h)
    print(s , "->",  d)
    tower(n-1,h,s,d,)

tower(3,'A','B','C')
# code of factorial using recursion 
#'''def factorial(n):
#    if( n == 0 or n == 1):
#        return 1
#    return n * factorial(n-1)

#n = int(input("Enter the number"))
# use of the lambda function
#print (factorial(n))'''
#print(x(2,3,5))
#x = lambda a,b,c : a + b + c 