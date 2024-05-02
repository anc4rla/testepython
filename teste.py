meu_dicionario = {1: 1, 2: 2, 3: 3}
chaves = meu_dicionario.keys()
soma_chaves = sum(chaves)
print(chaves)
print(soma_chaves)

dicionario_de_frutas = {"maçã": "vermelha", "banana": "amarela", "laranja": "laranja"}
dicionario_de_frutas["blueberry"] = "azul"
print(dicionario_de_frutas)

def calcular_quadrado(numero):
    return numero ** 2

numeros = [1, 2, 3, 4, 5]
quadrados = list(map(calcular_quadrado, numeros))
print(quadrados)

capitais = {"Irlanda": "Dublin", "Alemanha": "Berlim", "Japão": "Tóquio"}
capital_ir = capitais["Irlanda"]
print(capital_ir)

senhapadrão = "admin"
usuáriopadrão = "admin"

x = str(input("Insira seu nome de usuário: "))
y = str(input("Agora insira sua senha: "))
if x == usuáriopadrão and y == senhapadrão:
   print(True)
   print("Bem-vindo(a)")
if x == usuáriopadrão and y == senhapadrão:
  print("Explore nosso menu e escolha o número equivalente à opção desejada: ")
  print("1. Cadastro direto")
  print("2. Cadastro direto")
  print("3. Cadastro de aluno")
  print("4. Calculadora")
  y = float(input(""))

  if y == 1:
    print("Você escolheu o cadastro direto. Insira seu nome, senha e tipo de ID")
    q = input("Digite aqui seu nome: ")
    print(q)
    w = input("Digite aqui seu tipo de ID: ")
    print(w)
    e = input("Digite aqui sua senha: ")
    print(e)

  elif y == 2:
    print("Você escolheu o cadastro de professor. Insira seu nome, a matéria que você leciona, sua senha e seu ID")
    r = input("Digite aqui seu nome: ")
    print(r)
    t = input("Digite aqui a matéria que você leciona: ")
    print(t)
    u = input("Digite aqui seu tipo de ID: ")
    print(u)
    i = input("Digite aqui sua senha: ")
    print(i)

  elif y == 3:
    print("Você escolheu o cadastro do aluno. Digite aqui a matéria, seu nome de usuário, seu ano e sua senha")
    o = input("Digite aqui a matéria: ")
    print(o)
    a = input("Digite aqui o seu nome de usuário: ")
    print(a)
    s = input("Digite aqui seu ano: ")
    print(s)
    d = input("Digite aqui sua senha: ")
    print(d)

  elif y == 4:
    print("Você escolheu calculadora. Digite seus valores e realize sua operação")
    x = float(input("digite seu primeiro número: "))
    print("\n")
    y = float(input("digite seu segundo número: "))
    print("\n")
    print("- Adição")
    print("\n")
    print("- Subtração")
    print("\n")
    print("- Divisão")
    print("\n")
    print("- Multiplicação")
    print("\n")

    z = str(input("Digite a operação desejada(iniciando com letra maiúscula): "))

    if z == "Adição":
     print(x+y)

    elif z == "Subtração":
     print(x-y)

    elif z == "Divisão":

     if y != 0:
      print(x/y)

     else:
      print("Erro: divisão por zero")

    elif z == "Multiplicação":
     print(x*y)

else:
  print(False)
  print("Senha ou usuário incorretos, retorne e tente novamente")

