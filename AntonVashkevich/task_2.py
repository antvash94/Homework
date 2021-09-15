my_string = input("string:")
char_freq = dict.fromkeys(list(my_string), 0)
for i in my_string:
    char_freq[i] += 1
print(char_freq)
