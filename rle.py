def compress_rle(data: str) -> str:
    """Compression simple avec Run-Length Encoding (RLE)."""
    if not data:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed.append(data[i - 1] + str(count))
            count = 1

    compressed.append(data[-1] + str(count))
    return "".join(compressed)


def decompress_rle(compressed: str) -> str:
    """Décompression de la chaîne encodée en RLE."""
    if not compressed:
        return ""

    decompressed = []
    i = 0
    while i < len(compressed):
        char = compressed[i]
        count = ""
        i += 1
        while i < len(compressed) and compressed[i].isdigit():
            count += compressed[i]
            i += 1
        decompressed.append(char * int(count))

    return "".join(decompressed)


# Exemple d'utilisation
data = "AAAABBBCCDAA"
compressed_data = compress_rle(data)
decompressed_data = decompress_rle(compressed_data)

print(f"Original: {data}")
print(f"Compressé: {compressed_data}")
print(f"Décompressé: {decompressed_data}")

# Vérification
assert decompressed_data == data
