import simplecrypt

with open("encrypted.bin", "rb") as inp:

    encrypted = inp.read()
    print(simplecrypt.encrypt(encrypted))