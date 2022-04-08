#Taking input for matrix size
rows=int(input("Enter the rows:- "))
cols=int(input("Enter cols:- "))
line=50*'='
#initialize matrix list and temp 
matrix=[]
temp=[[0,0,0],[0,0,0],[0,0,0]]
#Entering value to matrix
for i in range(rows):
    mylist=[]
    for j in range(cols):
        x=int(input("Enter the item: "))
        mylist.append(x)
    matrix.append(mylist)    

#printing matrix
print(line)
print("Matrix is:-")
print(line)
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end='\t')
    print("")  
print(line)

#sum of row
for i in range(rows):
    sum=0
    for j in range(cols):
        sum+=matrix[i][j]

    print(i+1,"st row sum is:-",sum)
print(line)
#sum of col
for i in range(cols):
    sum=0
    for j in range(rows):
        sum+=matrix[j][i]
    print(i+1,"th col sum is:- ",sum)    
print(line)
#diagonal sum from another side
if rows==cols :
    sumr=0
    suml=0
    for i in range(rows):
       for j in range(cols):
            if(i==j):
                sumr+=matrix[i][j]
            
            if((i+j)==(rows-1)):
              suml+=matrix[i][j]    
    print("Sum of right diagonal is:",sumr)
    print("Sum of left diagonal is:",suml)            
    print(line)    
else:
    print("Not possible")                

#highest and lowest from eaach row
for i in range(rows):
    min=matrix[i][0]
    max=matrix[i][0]
    for j in range(cols):
       if(matrix[i][j]<min):
           min=matrix[i][j]
       if(matrix[i][j]>max):
           max=matrix[i][j]    
    print("Row ",i,":","Minimum is:",min,"Maximum is:",max)
    print(line)
#highest and lowest from whole matrix
min=max=matrix[0][0]
for i in range(rows):
    
    for j in range(cols):          
        if(matrix[i][j]<min):
            min=matrix[i][j]
        if(matrix[i][j]>max):
            max=matrix[i][j]

print(line)
print("Minimum is:",min,"Maximum is:",max)                



#transpose of Matrix
for i in range(cols):
    #templist=[]
    for j in range(rows):
        #templist.append()
        temp[j][i]=matrix[i][j]
#printing transpose matrix
print(line)
print("Transpose Matrix is")
print(line)        
for i in range(cols):
     for j in range(rows):
         print(temp[i][j],end='\t')
     print("")    