inp = (input("Put in 12 numbers: "))
#print(inp)
temp = inp.split()
lst2=[]
for i in range(len(temp)):
    lst2.append('_')
    print("_ ", end='')
count = 5
score = 0
print("\n")
while (count != 0):
    inp2 = (input("Your guess: "))

    count -=1
    if (inp2 in temp):
        for i in range (len(temp)):
            if(temp[i] == inp2):
                score +=1
                lst2[i] = temp[i]

        print(' '.join(lst2))
    else:
        lst2.append(inp2)
        print(' '.join(lst2))

print("Score: ",score)