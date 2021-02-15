import string
alphabet=string.ascii_lowercase
alphabet_list=list(alphabet)
string1=input()
string2=input()
list1=list(string1.lower())
list2=list(string2.lower())
l=len(list1)
if list1==list2:
    print("0")
else:
    for i in range(l):
        if list1[i]!=list2[i]:
            index1 = alphabet_list.index(list1[i])
            index2 = alphabet_list.index(list2[i])
            if index1 > index2:
                print("1")
                break
            elif index2 > index1:
                print("-1")
                break
