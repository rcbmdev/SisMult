"""
Modo de Operação:
r - read
w - write
a - append
"""
with open("dados/msg.txt",
          "r",
          encoding="utf-8") as f:
    for linha in f:
        print(linha)