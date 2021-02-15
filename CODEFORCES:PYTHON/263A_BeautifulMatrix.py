row1=input().split(" ")
row2=input().split(" ")
row3=input().split(" ")
row4=input().split(" ")
row5=input().split(" ")
matrix=[row1,row2,row3,row4,row5]
coordinate=[]
for i in range(5):
    if "1" in matrix[i]:
        x=matrix[i].index("1")
        coordinate.append(x-2)
        coordinate.append(i-2)
output=abs(coordinate[0])+abs(coordinate[1])
print(output)





