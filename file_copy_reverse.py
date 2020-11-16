with open('passwords.txt', 'r') as f:
    file_arr = []
    for x in f:
        file_arr.append(x)
    for x in reversed(file_arr):
        with open('output.txt','a') as f_second:
            f_second.write(x)
            print(x)