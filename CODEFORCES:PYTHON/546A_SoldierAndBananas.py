i=input()
i_list=i.split(" ")
cost_of_first_banana=int(i_list[0])
money_he_has=int(i_list[1])
number_of_bananas=int(i_list[2])
total_price=0
for i in range(1,number_of_bananas+1):
    total_price+=i*cost_of_first_banana
money_borrowed=total_price-money_he_has
if money_borrowed>0:
    print(money_borrowed)
else:
    print(0)
