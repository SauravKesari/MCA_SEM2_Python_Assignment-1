myList=[1,'a',4.4,4,[2,3,4]]
int_count=str_count=float_count=list_count=0
for i in range(len(myList)):
    if(isinstance(myList[i],int)):
        int_count+=1
    if(isinstance(myList[i],str)):
        str_count+=1
    if(isinstance(myList[i],float)):
        float_count+=1
    if(isinstance(myList[i],list)):
        list_count+=1

print("Total Elements:",len(myList))
print("Integer count:  ",int_count)
print("String count:  ",str_count)
print("Float count: ",float_count)
print("List count: ",list_count)


                    
        
