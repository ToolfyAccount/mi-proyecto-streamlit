from bitstring import BitArray

texto = "Prueba"
binario = ' '.join(BitArray(bytes=c.encode()).bin for c in texto)
print(binario)