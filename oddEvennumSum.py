num=int(input("Enter the Number"))
sum_even=0
sum_odd=0
count_even=count_odd=count=0
while(num>0):
    if(num%2==0):
        sum_even+=num
        count_even+=1
    else:
        sum_odd+=num
        count_odd+=1    
    count+=1
    num=int(input("Enter number"))

print("Sum of Even Numbers are:",sum_even)
print("Sum of odd Numbers are:",sum_odd)
print("Total Even Numbers:",count_even)
print("Total odd Numbers are:",count_odd)
print("Total Numbers are: ",count)