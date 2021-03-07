print("Hello Yogesh")


def greet():
    print("Hello Sachin")
    print("How are you")
    print("Hope you doing well")


def greet_with_name(name):
    print(f"hello {name}")
    print(f"How are you: {name}")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what it is like in {location}")


greet()
greet_with_name("Yogesh")
greet_with(location="Diveagar", name="Kaminee" )


h = int(input("Please enter height of wall"))
w = int(input("Please enter width of wall"))


import math
def paint_calc(height,width,coverage):
    area = height * width
    num_of_can = math.ceil(area/coverage)
    print(f"number of can required are {num_of_can}")


paint_calc(h, w, 5)


def find_prime_numbers():
    number = int(input("Please enter the number"))

    for n in range(2,number):
        if number % n==0:
            print("number is not a prime number")
            break
    else:
        print("Number is prime number")


find_prime_numbers()


# Cipheer code
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    encrpted_text=""
    for ele in text:
        index = alphabet.index(ele)+shift
        encrpted_text+=alphabet[index]

    return encrpted_text



def decrypt(text,shift):
    decrpted_text=""
    for ele in text:
        index = alphabet.index(ele)-shift
        decrpted_text+=alphabet[index]

    return decrpted_text

if direction == 'encode':
    encrypted_text = encrypt(text,shift)
    print("Entrypted text"+str(encrypted_text))
elif direction == 'decode':
    decrypted_text = decrypt(text,shift)
    print("decrypted text"+str(decrypted_text))
else:
    print("PLease enter valid directions 1.encode 2.decode")