for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
print("".join(chr(letter) for letter in range(97, 123)))