login=False
while login==False :
    Username=input("Username:")

    if Username.isalpha():
       login=True

    else:
        print("you user name must be all in alphabetical,please try again~")
        login=False

check_password=False
while check_password==False :
    Password=input("Password:")

    if (Password.isnumeric() and len(Password)>=5):
       check_password=True
       
    else:
        print("you Password must be at least 5 characters and must be numeric, please try again~")
        check_password=False

