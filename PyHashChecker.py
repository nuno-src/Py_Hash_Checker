


h1 = input("Insira a 1º hash: ")

h2 = input("Insira a 2º hash: ")


# Hash
hah_h1 = hash(h1)

hah_h2 = hash(h2)

# print(hah_h1)
# print(hah_h2)

# Versão 1:

if h1 == h2 and hah_h1 == hah_h2:
    print("\nAs Hash's são Iguais.")
else:
    print("\nATENÇÃO as Hash's SÃO DIFERENTES!!!")



