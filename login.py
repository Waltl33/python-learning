print("Create account now")
username = input ("Enter user name: ")
password = input ("Enter password: ")

print("Your account has been created successfully")
print("Login now!")

username2 = input("Enter username: ")
password2 = input ("Enter password: ")

if username == username2 and password == password2:
    print("Login successfull")
else:
    print("Invalid credentials")
