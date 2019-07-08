correct_password = "python123"
name = input("Enter First Name: ")
surname = input("Enter Surname: ")
password = input("Enter Password:")

while correct_password != password:
    password = input("Wrong Password! Enter again:")

message = ("Hi %s %s, you are logged In" %(name, surname))
print(message)
