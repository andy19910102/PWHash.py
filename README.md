# PWHash.py

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

```python
from pw_hash import PWHash

password = "12345678"

pw_hash = PWHash(password)

print(pw_hash.check_password("123456"))
print(pw_hash.check_password("1234567"))
print(pw_hash.check_password("12345678"))
```