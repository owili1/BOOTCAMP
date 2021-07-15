num1=int(input("Please enter num1"))
num2=int(input("Please enter num2"))
num3=int(input("Please enter num3"))
if num1==num2==num3:
    print("Are Equal")
else:
    print("Not equal")


#Question 5
j=0
for i in range(0,10):
    j+=1
    print(j)
    

    j=1
    for i in range(0,10):
        j+=j
        print(j)
        

        for j in range(0,10):
            j+=j
            print(j)

#Question 6
n=123456789  
m=0
while n!=0:
    m=(10*m)+(n%10)
    n//=10
    print(m)
    print(n) 

 #Question 7
f=0
g=1
for i in range (0,16):
    f=f+g
    g=f-g
    stdio.writeln(f)    


