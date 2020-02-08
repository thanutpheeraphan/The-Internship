## Question1
words = []
lines = int(input("Input No. of lines: "))
cap_words = [""] * lines

for i in range(lines):
    word_input = input("Word: ")
    words.append(word_input)

for i in range(lines):
    for letter in words[i]:
        if (letter.isupper()):
            cap_words[i] += letter

cap_words.sort(key = len)
cap_words.reverse()
print(cap_words)



