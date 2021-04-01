print("a) Write a python program to print the square of all numbers from 0 to 10")

square=[0,1,2,3,4,5,6,7,8,9,10]
x=0
number=0
for num in square:
    number=x*x
    print("The square of "+str(num)+ "is:"+str(number))
    x=x+1

print("\n"+"b) Write a python program to find the sum of all even numbers from 0 to 10")
for num in square:
    if(num % 2 ==0):
        print("even nuber 0-10 have:"+str(num))