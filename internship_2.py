
def check_prime(num):
    for i in range(2, num // 2):
        if (num % i) == 0:
            return False
    else:
        return True
inp = 5
while(True):
    inp = input("Enter a number : ")
    if(inp == 0.0 or inp =="0.0"):
        exit()
    lst= []
    for i in range (len(inp)):
        if(inp[i]=='.'):
            pass
        else:
            lst.append(inp[i])

    i=0
    a = int((lst[i]) + (lst[i + 1]))
    b = int((lst[i]) + (lst[i + 1])+(lst[i+2]))
    c = int((lst[i]) + (lst[i + 1])+(lst[i+2])+(lst[i+3]))
    if (check_prime(a)==True):
        print("TRUE")
    else:
        if(check_prime(b)==True):
            print("TRUE")
        else:
            if (check_prime(c) == True):
                print("TRUE")
            else:
                print("FALSE")

