
print("For sin continue")

for i in range(1,11):

    if i % 2 ==0:
        print(i, end=" ")


print("")

print("For sin continue")
for i in range(1,11):
    if i % 2 !=0:
        continue
    print(i, end=" ")

print("")
print("While sin continue")


numero = 0

while numero <10:

    numero = numero + 1
    if numero % 2 ==0:

        print(numero, end=" ")


print("")
print("While con  continue")

i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i, end=" ")
