inp = int(input("Put in num of lines: "))
lst1=[]
order_list = []
for i in range (inp):
    temp = input("Put in word: ")
    lst1.append(temp)

for i in range(inp):
    final_lst = []
    temp  = lst1[i]
    temp = temp.split()
    #print(temp,"temp")
    for i in range (len(temp)):
        temp2 = temp[i]
        #print(temp2,"temp2")
        j=0
        #print(temp2[j],"temp2[j]")
        if(temp2[j].isupper()):
            final_lst.append(temp2[j])
    order_list.append(''.join(final_lst))
    #print(''.join(final_lst)," final lst")
    #print("\n")


def order(lst):
    lst.sort(key=len)
    lst.reverse()
    return lst

#print("OrderList", order_list)
to_print = (order(order_list))
for i in range (len(to_print)):
    print(to_print[i])

#print(lst1)

