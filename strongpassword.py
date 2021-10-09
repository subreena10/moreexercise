strong_password=input("Enter ur password:")

if len(strong_password) is "6" or "16":
    if "A" or "Z" in  strong_password :
        if "$" in  strong_password :
            if "2" or "8" in  strong_password :
                    print("your password is strong.")
            else:
                    print("your password is not strong")
        else:
                print("medium password.")
    else:
            print("create a strong password.")
else:
    print("passwrd is not strong. ")