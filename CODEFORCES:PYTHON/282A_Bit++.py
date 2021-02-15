n_lines=int(input())
x=0
for i in range(n_lines):
    statement=input()
    if statement[1]=="+":
        x+=1
    else:
        x-=1
print(int(x))

