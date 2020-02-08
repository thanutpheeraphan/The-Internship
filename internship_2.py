##Question 2

LIMIT = 5
def check_prime(num: int) -> bool:
    for i in range(2, num // 2):
        if (num % i) == 0:
            return False
    else:
        return True

def addList(lst: list) -> int:
    return int(lst[0:2]),\
           int(lst[0:3]),\
           int(lst[0:4])

def inputValidate(s: str) -> bool:
    if (s is "0.0"):
        exit()
    elif (len(s) < LIMIT):
        exit()
    return True


while(True):
    inp = input("Enter a decimal number : ")

    inputValidate(inp)

    num = ""
    for i in range (LIMIT):
        if(inp[i]=='.'):
            pass
        else:
            num += inp[i]

    two_digit, three_digit, four_digit = addList(num)

    if (check_prime(two_digit) or check_prime(three_digit) or check_prime(four_digit)):
        print("TRUE")
    else:
        print("FALSE")

