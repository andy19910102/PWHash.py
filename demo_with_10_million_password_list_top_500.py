import requests
from pw_hash import PWHash

password_txt_source_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-500.txt"

res = requests.get(password_txt_source_url)
password_list = res.text.split()
hash_list = []

for password in password_list:
    pw_hash = PWHash(password)
    hash_list.append(pw_hash)

print(hash_list)
