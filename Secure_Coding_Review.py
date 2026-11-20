
# Secure Coding Review
# Example of Insecure Code

username = input("Enter username: ")
password = input("Enter password: ")

# Insecure: Hardcoded password
admin_password = "admin123"

if password == admin_password:
    print("Login Successful")
else:
    print("Invalid Password")

# Insecure: Displaying sensitive information
print("Your password is:", password)
