n = int(input())

for i in range(n):
    password = input()

    passwordLen = len(password)
    if passwordLen < 6:
        print("Your password is tai duan le.")
    else:
        array = [0] * 4

        for j in range(passwordLen):
            if password[j] == ".":
                array[0] = 1
            elif ((password[j] >= "a" and password[j] <= "z") or (password[j] >= "A" and password[j] <= "Z")):
                array[1] = 1
            elif password[j] >= "0" and password[j] <= "9":
                array[2] = 1
            else:
                array[3] = 1

        if array[3] == 1:
            print("Your password is tai luan le.")
        elif array[2] == 0:
            print("Your password needs shu zi.")
        elif array[1] == 0:
            print("Your password needs zi mu.")
        else:
            print("Your password is wan mei.")
