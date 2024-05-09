for i in range(5):
    if i == 3:
      print("Atingiu o número 3, interrompendo o loop.")
      break
    else:
      print("Número:",i)

for i in range(5):
    if i == 2:
      print("Pulando a iteração",i)
      continue
      print("Número:",i)

minha_lista = [1,2,3,4,5]
for item in minha_lista:
   if item % 2 == 0:
      pass
   else:
      print("ímpar", item)

estoque_frutas = {'Abacaxi':10, 'Morango':20, 'Uva':15}
for fruta, quantidade in estoque_frutas.items():
   print(f'fruta:{fruta},quantidade:{quantidade}')

for numero_coluna1 in range(2,5):
   print("tabuada do", numero_coluna1)
   for numero_coluna2 in range(11):
      print(numero_coluna1, "x", numero_coluna2, "=", numero_coluna1 * numero_coluna2)