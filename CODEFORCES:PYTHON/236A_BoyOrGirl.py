username=input()
letters_list=[]
count=0
for u in username:
    if u not in letters_list:
        letters_list.append(u)
        count+=1
if count%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")