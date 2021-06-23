def exec01():
  # Desenvolver um programa que pergunte ao usuário o seu nome 
  # completo e seu sexo. Em seguida,
  # o programa deve apresentar os dados anteriormente informados.
  nome = input("Digite seu nome: ")
  sexo = input("Digite seu sexo: ")

  print(f"Seu nome é '{nome}' e seu sexo é '{sexo}'")

def exec02():
  #2) Elaborar um programa que pergunte quatro valores inteiros e apresente 2 resultados:
  #a) Resultado de suas adições
  #b) Resultado de suas multiplicações
  soma = 0
  mult = 1

  for i in range(4):
    n = int(input("Digite um número: "))
    soma += n
    mult *= n
  
  print(f"A soma dos números é {soma}.")
  print(f"A multiplicação dos números é {mult}.")


print('''
###########
Escolha qual exercício deseja executar:
1- Imprime infos
2- Calcula soma e mult
''')
quest = int(input())

if quest == 1: exec01()
if quest == 2: exec02()