# Decimal Conversion Functions
def decimal_to_binary(num):
    return bin(num)[2:]
def decimal_to_octal(num):
    return oct(num)[2:]
def decimal_to_hex(num):
    return hex(num)[2:].upper()

# Binary Conversion Functions
def binary_to_decimal(binary_str):
    return int(binary_str, 2)

# Octal Conversion Functions
def octal_to_decimal(octal_str):
    return int(octal_str, 8)

# Hex Conversion Functions
def hex_to_decimal(hex_str):
    return int(hex_str, 16)
