num=int(input("Enter the Number"))
while(num>0):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
           # print("true")
        
    if(count==2):
        print("No is prime")
    else:
        print("No is not prime")           

    num=int(input("Enter number"))

#print("Sum of Numbers are:",sum)
#print("Total Numbers are: ",count)