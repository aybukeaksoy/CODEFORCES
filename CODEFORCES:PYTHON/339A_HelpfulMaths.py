string=input()
string_list=list(string)
swapped=True
output=""
while swapped:
    swapped=False
    for i in range(len(string)-2):
        if string_list[i]>string_list[i+2]:
            string_list[i],string_list[i+2]=string_list[i+2],string_list[i]
            swapped=True
for s in string_list:
    output+=s
print(output)


