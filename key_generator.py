import random
import string

print("=== GERADOR DE SENHA ALEATÓRIA ===\n")
print("INFORME COM 's' ou 'n' se a senha receberá: \n")

print("-"*30)
l_select = str(input("> Letras MINÚSCULAS (s/n): "))

if(l_select != "s" and l_select != "n"):
  while(l_select != "s" and l_select != "n"):
    print("\nCOMANDO INVÁLIDO!")
    l_select = str(input("\n> Letras MINÚSCULAS (s/n): "))

if(l_select == "s"):
  lower = string.ascii_lowercase
else:
  lower = ""

print("-"*30)
u_select = str(input("> Letras MAIÚSCULAS (s/n): "))

if(u_select != "s" and u_select != "n"):
  while(u_select != "s" and u_select != "n"):
    print("\nCOMANDO INVÁLIDO!")
    u_select = str(input("\n> Letras MAIÚSCULAS (s/n): "))

if(u_select == "s"):
  upper = string.ascii_uppercase
else:
  upper = ""

print("-"*30)
n_select = str(input("> NÚMEROS (s/n): "))

if(n_select != "s" and n_select != "n"):
  while(n_select != "s" and n_select != "n"):
    print("\nCOMANDO INVÁLIDO!")
    n_select = str(input("\n> NÚMEROS (s/n): "))

if(n_select == "s"):
  numbers = '0123456789'
else:
  numbers = ""

print("-"*30)
s_select = str(input("> SÍMBOLOS (s/n): "))

if(s_select != "s" and s_select != "n"):
  while(s_select != "s" and s_select != "n"):
    print("\nCOMANDO INVÁLIDO!")
    s_select = str(input("\n> SÍMBOLOS (s/n): "))

if(s_select == "s"):
  symbols = str(input("> Defina quais símbolos podem ser usados: "))
else:
  symbols = ""

print("-"*30)
key_len = int(input("> Informe o TAMANHO da senha (maior que 5): "))

if(key_len < 5):
  while(key_len < 5):
    print("\nTAMANHO INVÁLIDO!")
    key_len = int(input("\n> Informe o TAMANHO da senha (maior que 5): "))

key_char = lower + upper + numbers + symbols

key = "".join(random.sample(key_char, key_len))

print("-"*30)
print("\nSENHA ALEATÓRIA GERADA:", key)