from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes



# 사용할 키 생성
input_str = "2019125007KIMKYU"

# 이진수 문자열 생성 (128비트로 제한)
binary_key = ''.join('{:08b}'.format(ord(char)) for char in input_str)[:128]

# 이진수 문자열을 바이트로 변환
key_bytes = bytes(int(binary_key[i:i + 8], 2) for i in range(0, len(binary_key), 8))

# 평문
plaintext = "ABCDEFGHIJKLMNOP"
plaintext_bytes = plaintext.encode('utf-8')

# 패딩 생성 
def pad(text):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(text) + padder.finalize()
    return padded_data

iv = b'\x00' * 16  
cipher = Cipher(algorithms.AES(key_bytes), modes.CFB(iv))

# 암호화 
encryptor = cipher.encryptor()
padded_data = pad(plaintext_bytes)
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

# 암호화 결과 출력
print("암호문:")
print(ciphertext.hex())


### 여기부터 복호화 
# AES 복호화
decryptor = cipher.decryptor()
decrypted_padded_data = decryptor.update(ciphertext) + decryptor.finalize()

# 패딩 제거
def unpad(text):
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(text) + unpadder.finalize()
    return unpadded_data

# 복호화된 데이터를 다시 문자열로 디코딩
decrypted_data = unpad(decrypted_padded_data)
decrypted_plaintext = decrypted_data.decode('utf-8')

# 결과 출력
print("복호화된 평문:")
print(decrypted_plaintext)



legacy_ciphertext=ciphertext

# 평문 이진수 변환
plaintext_binary = ''.join('{:08b}'.format(ord(char)) for char in plaintext)[:128]

# 첫 번째 비트 수정 후 암호화 (0->1)
changed_plaintext_binary = '1' + plaintext_binary[1:]
changed_plaintext= bytes(int(changed_plaintext_binary[i:i + 8], 2) for i in range(0, len(changed_plaintext_binary), 8))
iv = b'\x00' * 16  
cipher = Cipher(algorithms.AES(key_bytes), modes.CFB(iv))

# 암호화 
encryptor = cipher.encryptor()
padded_data = pad(changed_plaintext)
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

# 수정 후 암호화 결과 출력
print("수정 후 암호문:")
print(ciphertext.hex())


# 변경된 비트의 수 계산
different_bits_count = sum(bit1 != bit2 for bit1, bit2 in zip(legacy_ciphertext, ciphertext))

# 결과 출력
print("비트 달라진 수:", different_bits_count)



######## 암호 키 수정하기


# 이진수 문자열을 바이트로 변환
changed_key=  '1' + binary_key[1:]
key_bytes = bytes(int(changed_key[i:i + 8], 2) for i in range(0, len(changed_key), 8))

# 패딩 생성 
def pad(text):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(text) + padder.finalize()
    return padded_data
iv = b'\x00' * 16  
cipher = Cipher(algorithms.AES(key_bytes), modes.CFB(iv))

# 암호화 
encryptor = cipher.encryptor()
padded_data = pad(plaintext_bytes)
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

# 암호화 결과 출력
print("키 수정 후 암호문:")
print(ciphertext.hex())

different_bits_count = sum(bit1 != bit2 for bit1, bit2 in zip(legacy_ciphertext, ciphertext))

# 결과 출력
print("비트 달라진 수:", different_bits_count)

