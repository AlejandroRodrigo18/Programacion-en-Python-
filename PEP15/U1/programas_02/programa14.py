bytes_input = int(input("Introduce el número de bytes: "))

# Sistema decimal

gb_si = bytes_input // 1_000_000_000
mb_si = (bytes_input % 1_000_000_000) // 1_000_000
kb_si = (bytes_input % 1_000_000) // 1_000
b_si = bytes_input % 1_000

# Sistema binario

gib_iec = bytes_input // (1024**3)
mib_iec = (bytes_input % (1024**3)) // (1024**2)
kib_iec = (bytes_input % (1024**2)) // 1024
b_iec = bytes_input % 1024

print(f"{bytes_input} bytes en sistema decimal (SI): {gb_si} GB, {mb_si} MB, {kb_si} KB, {b_si} bytes")
print(f"{bytes_input} bytes en sistema binario (IEC): {gib_iec} GiB, {mib_iec} MiB, {kib_iec} KiB, {b_iec} bytes")
