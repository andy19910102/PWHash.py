import requests
from pw_hash import PWHash
import csv

password_txt_source_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-500.txt"

res = requests.get(password_txt_source_url)
password_list = res.text.split()
hash_list = []

csv_header = ["Password", "Prefix Salt", "Suffix Salt", "Hash"]
with open('countries.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(csv_header)
    for password in password_list:
        # Using testing mod to create PWHash Object
        # You will be able to get the prefix, suffix and hashed_password
        # from the PWHash Object
        pw_hash = PWHash(password, mod="testing")
        hash_list.append(pw_hash)
        row = [password, pw_hash.prefix, pw_hash.suffix, pw_hash.hashed_password]
        writer.writerow(row)
