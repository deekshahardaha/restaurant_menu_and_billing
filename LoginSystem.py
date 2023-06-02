user = ['alice', 'bob', 'john', 'martin', 'peter', 'joseph']
passwords = {'alice': '123', 'bob': '456', 'john': '789', 'martin': '246', 'peter': '369', 'joseph': '1357'}
department = {"admin": ['alice', 'bob', 'martin'], 'student': ['bob', 'john', 'peter', 'joseph']}
name = input("Enter username : ")
if name in user:
    passw = input("Enter password : ")
    if passw == passwords[name]:
        dept = input("Enter department :").lower()
        if dept in department:
            if name in department[dept]:
                print(f"Login successful as {dept}")
            else:
                print("User does not belongs to department entered")
        else:
            print("Department does not exist")
    else:
        print("Incorrect password")
else:
    print("Invalid username")
