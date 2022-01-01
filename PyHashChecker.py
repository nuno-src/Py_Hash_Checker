


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


# Versão 2:
# 
# v1 = []
# def check1():
#     if h1 == h2:
#         print("\nVerificação string... (1/2) - Pass")
#         v1.append(1)
#     else:
#         print("\nVerificação string... (2/2) - Fail")
# 
# 
# check1()
# 
# v2 = []
# def check2():
#     if hah_h1 == hah_h2:
#         print("\nVerificação hash... (2/2) - Pass")
#         v2.append(1)
#     else:
#         print("\nVerificação hash... (2/2) - Fail")
# 
# 
# check2()
# 
# 
# # print(v1)
# # print(v2)
# 
# try:
#     if v1[0] == 1 and v2[0] == 1:
#         print("\nAs Hash's são Iguais.")
# except:
#     print("\nATENÇÃO as Hash's SÃO DIFERENTES!!!")


