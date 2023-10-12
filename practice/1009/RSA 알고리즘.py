import random

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    max_divisor = int(num ** 0.5) + 1
    for i in range(3, max_divisor, 2):
        if num % i == 0:
            return False
    return True

def calculate_gcd(a, b):
    if b == 0:
        return a
    return calculate_gcd(b, a % b)

def mod_inverse(e, phi_n):
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            gcd, x, y = extended_gcd(b % a, a)
            return (gcd, y - (b // a) * x, x)

    gcd, x, _ = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError("The modular inverse does not exist")
    else:
        return x % phi_n

def encrypt(message, public_key):
    e, n = public_key
    cipher_text = [pow(ord(pair), e, n) for pair in message]
    return cipher_text

def decrypt(cipher_text, private_key):
    d, n = private_key
    decrypted_text = [chr(pow(pair, d, n)) for pair in cipher_text]
    return ''.join(decrypted_text)

def generate_keys(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 2
    while e < phi_n and calculate_gcd(e, phi_n) != 1:
        e += 1
    d = mod_inverse(e, phi_n)
    return ((e, n), (d, n) )


def encrypt_student_id(student_id, public_key):
    pairs = [student_id[i:i+2] for i in range(0, len(student_id), 2)]
    encrypted_id = [str(pow(int(''.join(pair)), public_key[0], public_key[1])).zfill(2) for pair in pairs]
    return encrypted_id


def decrypt_student_id(encrypted_id, private_key):

    decrypted_pairs = [str(pow(int(pair), private_key[0], private_key[1])).zfill(2) for pair in encrypted_id]
    return ''.join(decrypted_pairs)


p = 7
q = 17

public_key, private_key = generate_keys(p, q)
print("Public key:", public_key)
print("Private key:", private_key)

student_id = "125007"

ciphered_id = encrypt_student_id(student_id, public_key)
print("암호화 후 학번:", ciphered_id)

decrypted_id = decrypt_student_id(ciphered_id, private_key)
print("복호화 후 학번:", decrypted_id)
