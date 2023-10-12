# Input string
input_str = "2019125007KIMKYU"


binary_key = ' '.join('{:08b}'.format(ord(char)) for char in input_str)

print("ASCII Codes  2019125007KIMKYU:")
print(binary_key)

