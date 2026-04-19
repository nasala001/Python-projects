print("*** PASSWORD CHECKER ***")
password = input("Enter password: ")

A = False   # lowercase letter found
B = False   # number found
C = False   # special character found

size = len(password)


for i in range(0, size):
    if password[i] >= "a" and password[i] <= "z":
        A = True
    elif password[i] >= "0" and password[i] <= "9":
        B = True
    else:
        C = True


if size >= 10 and A and B and C:
    print("Valid password!")
else:
    print("Invalid password!")
    if size < 10:
        print("- Must be at least 10 characters")
    if not A:
        print("- Must contain a lowercase letter")
    if not B:
        print("- Must contain a number")
    if not C:
        print("- Must contain a special character (!@#$ etc.)")