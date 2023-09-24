current_char = 'A'
current_num = 1

for i in range(5):
    for j in range(i + 1):
        if i % 2 == 0:
            print(current_char, end=' ')
            current_char = chr(ord(current_char) + 1)
        else:
            print(current_num, end=' ')
            current_num += 1
    print()
