str_user = input()

if str_user.isalpha():
    if "a" in str_user or "o" in str_user:
        if "i" not in str_user and "e" not in str_user:
            print(True)
        else:
            print(False)
    else:
        print(False)
