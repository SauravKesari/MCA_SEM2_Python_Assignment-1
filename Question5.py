#sum,average,count,min,max of list members
from itertools import count


mylist=[]
while(1):
    x=int(input("Enter element"))
    if x<0:
      break
    else:
        mylist.append(x)

#count no of elements
size=len(mylist)
print("No of elements are: ",size)        
#sum of elements
sum=0
for i in range(size):
  sum+=mylist[i]

print("Sum is ",sum)

#average of elements
avg=0.0
for i in range(size):
    avg=float(sum/size)

print(avg)

#count and sum of even and odd
sum_even=sum_odd=count_even=count_odd=0
for i in mylist:
    if(i%2==0):
        count_even+=1
        sum_even+=i
    else:
        count_odd+=1
        sum_odd+=i
print("Total Even Element: ",count_even)
print("Sum of Even Element: ",sum_even)
print("Total Odd Element: ",count_odd)
print("Sum of odd Element: ",sum_odd)

#largest and smalllest number
max=min=0
mylist.sort()
min=mylist[0]
max=mylist[size-1]

print("Smallest Element: ",min)
print("Largest Element: ",max)
