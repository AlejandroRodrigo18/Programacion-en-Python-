a = 34
a_binario = bin(a)
a_octal = oct(a)
a_hexadecimal = hex(a)


print(a,"en binario es: ",a_binario)
print(a, "en octal es:", a_octal)
print(a, "en hexadecimal es:", a_hexadecimal)

binario =  "0b1001"
octal = "0o12"
hexadecimal = "0xa3f"

numero_decimal= int(binario, 2)
numero_octal= int(octal, 8)
numero_hexadecimal= int(hexadecimal, 16)

print("")

print(a_binario, "en decimal es: ", numero_decimal)
print(a_octal, "en decimal es: ", numero_octal)
print(a_hexadecimal, "en decimal es: ", numero_hexadecimal)
