from pw_hash import PWHash

password = "12345678"

pw_hash = PWHash(password)

print(pw_hash)
print(dir(pw_hash))
print(pw_hash.check_password("123456"))
print(pw_hash.check_password("1234567"))
print(pw_hash.check_password("12345678"))