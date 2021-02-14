i=input()
space=i.index(" ")
m=int(i[:space])
n=int(i[space+1:])
if m%2==0 or n%2==0:
    output=m*n/2
else:
    output=max(m,n)//2*min(m,n)+min(m,n)//2

print(int(output))