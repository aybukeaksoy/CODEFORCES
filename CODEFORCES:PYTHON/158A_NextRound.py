i=input()
scores=input()
n=i[0]
k=i[2]
output=int(k)
scores_list=scores.split(" ")
for r in range(int(k),int(n)):
    if int(scores_list[r])<int(scores_list[int(k)-1]):
        break
    elif int(scores_list[r])==0:
        output=0
    elif int(scores_list[r])>0:
        output+=1


print(output)


