import sympy
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mult_inv(e, phi):
    d = sympy.mod_inverse(e, phi)
    return d

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = mult_inv(e, phi)
    return (n, e), (n, d)

def encrypt(string, public_key):
    n, e = public_key
    encrypted = [pow(ord(char), e, n) for char in string]
    return encrypted

def decrypt(encrypted_string, private_key):
    n, d = private_key
    decrypted = [chr(pow(char, d, n)) for char in encrypted_string]
    return ''.join(decrypted)

#Encryption
p = 13      #can generate random prime integers 
q = 19
public_key, private_key = generate_keypair(p, q)

string = "Encrypt this string"

encrypted_string = encrypt(string, public_key)
print("Encrypted string:", encrypted_string)

decrypted_string = decrypt(encrypted_string, private_key)
print("Decrypted string:", decrypted_string)