n_lines=int(input())
operation_list=[]
x=0
for i in range(n_lines):
    statement=input()
    for s in statement:
        if s!="x":
            operation_list.append(s)
plus_snum=operation_list.count("+")
minus_snum=operation_list.count("-")
last_operation=(max(plus_snum,minus_snum)-min(plus_snum,minus_snum))/2
if max(plus_snum,minus_snum)==plus_snum:
    x+=last_operation
else:
    x-=last_operation

print(int(x))

