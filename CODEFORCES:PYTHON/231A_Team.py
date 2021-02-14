n_lines=int(input())
answer_count=0
for i in range(n_lines):
    teams_view=input()
    view_list=[teams_view[0],teams_view[2],teams_view[4]]
    zero_view_count=view_list.count("0")
    if zero_view_count<=1:
        answer_count+=1
print(answer_count)



