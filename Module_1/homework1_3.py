left = input()
right = input()

bool_var = True

while True:
    user_num = input()
    if user_num == "":
        break
    if user_num.isdigit():
        user_num = int(user_num)
        left = int(left)
        right = int(right)
        if left <= user_num <= right:
            bool_var = True
        else:
            bool_var = False


print(bool_var)
