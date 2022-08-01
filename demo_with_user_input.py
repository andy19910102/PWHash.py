from pw_hash import PWHash

password = input("Please enter your password:")

pw_hash = PWHash(password)
print("pw_hash has been created successfully")

i = 0
check_limit = 5
while i < check_limit:
    print("*" * 30)
    input_password = input("Enter password for check:")
    if pw_hash.check_password(input_password):
        break
    i += 1
    print(f"Wrong password! You only have { check_limit - i} times to try.")
    

if i >= 5:
    print("You've run out all remaining opportunities to try.")
else:
    print("Great! the you enter the right password.")