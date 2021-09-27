
from string import ascii_lowercase, ascii_letters


class Cipher:
    def __init__(self, word):
        if all(i in ascii_letters for i in word):
            self.key_word = word.lower()
        else:
            raise TypeError("Only ascii letters")
        self.alphabet = ascii_letters
        self._cipher_template = self.key_word + "".join([i for i in ascii_lowercase if i not in self.key_word])
        self.cipher_alphabet = self._cipher_template.lower() + self._cipher_template.upper()

    def encode(self, text=""):
        tab = text.maketrans(self.alphabet, self.cipher_alphabet)
        result = text.translate(tab)
        return result

    def decode(self, text=""):
        tab = text.maketrans(self.cipher_alphabet, self.alphabet)
        result = text.translate(tab)
        return result


cipher = Cipher("crypto")
print(cipher.encode("Hello world"))
print(cipher.decode("Btggj vjmgp"))
print(cipher.decode("Fjedhc dn atidsn"))
