from string import ascii_letters, digits
from random import choice
from hashlib import sha256

class PWHash:
    def __init__(self, password: str, salt_len=15, mod="production"):
        """
        Create a PWHash object,
        mod="production" {default} | "testing"
        """
        salt_source = ascii_letters+digits
        prefix, suffix = "", ""
        i = 0
        while i < salt_len:
            prefix += choice(salt_source)
            suffix += choice(salt_source)
            i += 1
        salted_password = prefix + password + suffix
        hash_password = self.__create_hash(salted_password)
        self.__prefix = prefix
        self.__suffix = suffix
        self.__hashed_password = hash_password
        if mod == "testing":
            self.prefix = prefix
            self.suffix = suffix
            self.hashed_password = hash_password

    def __create_hash(self, input_txt: str) -> str:
        """
        Return a hash using sha256
        """
        hash_output = sha256(str(input_txt).encode('utf-8')).hexdigest()
        return hash_output

    def check_password(self, input_password: str) -> bool:
        """
        Check if input_password is the right password
        """
        input_hash = self.__create_hash(self.__prefix+input_password+self.__suffix)
        return self.__hashed_password == input_hash
        