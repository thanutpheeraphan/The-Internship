## Question 3
inp = (input("Put in 12 numbers: "))
inp_list = inp.split()
ans_list = ['_'] * 12

for _ in range (12):
    print("_ ", end='')
    
count = 5
score = 0
print()

while (count != 0):
    inp2 = (input("Your guess: "))
    count -= 1
    
    if (inp2 in inp_list):
        for i in range (len(inp_list)):
            if(inp_list[i] == inp2):
                score +=1
                ans_list[i] = inp_list[i]
    elif inp2 not in ans_list:
        ans_list.append(inp2)

    print(' '.join(ans_list))

print("Score: ",score)
