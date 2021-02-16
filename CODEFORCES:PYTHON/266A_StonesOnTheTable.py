count=0
number_of_stones=int(input())
colors_of_stones=input()
l=len(colors_of_stones)-1
for i in range(l):
    if colors_of_stones[i]==colors_of_stones[i+1]:
        count+=1
print(count)        