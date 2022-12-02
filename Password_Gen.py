
import random
import pyperclip as ppc

container = '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''*6

while True:
    length = int(input("\nPassword Length\n\n=> "))
    
    if length <= 500:
        password = "".join(random.sample(container, length))
        print(f"\nYour Password Is : {password}")
        copy = input("\nCopy To Clipboard (Y/n) : ").upper()
        if copy == "Y":
            ppc.copy(password)
            print("\nCopied Successfully!")
    
    else:
        print("\nMAX Length 500")

    new = input("\nGenerate New Password (Y/n) : ").upper()
    if new != "Y":
        break

