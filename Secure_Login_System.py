
# Secure Coding Review
# Secure Login System

username = input("Enter username: ")
password = input("Enter password: ")

admin_username = "admin"
admin_password = "Admin@123"

if username == admin_username and password == admin_password:
    print("Login Successful!")
else:
    print("Invalid Login!")

# Do not display the password
print("Password is protected.")

# Password validation
new_password = input("Create a new password: ")

if len(new_password) >= 8:
    print("Password Accepted!")
else:
    print("Password is too short!")
