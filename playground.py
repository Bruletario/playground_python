"""A=int(input())
B=int(input())
X=A+B
print("X = ",X)
print(f"X = {X}")"""

"""
n = 3.14159
raio = float(input())
a = n*raio**2
print(f"A={a:.4f}") #quando quero brecar as casas decimais preciso fazer a: .4(para 4 casas)f (porque é float) """

"""
a = int(input())
b = int(input())

produto = a*b

print("PROD =", produto)
"""
"""
a = float(input())
b = float(input())

mediaPonderada = ((a*3.5)+(b*7.5))/11

print(f"MEDIA = {mediaPonderada:.5f}")
"""
"""
numFuncionario = int(input())
horaTrabalhada = int(input())
valorHora = float(input())

salario = horaTrabalhada*valorHora

print(f"NUMBER = {numFuncionario}")
print(f"SALARY = U$ {salario:.2f}")
"""
"""
nomeVendedor = input()
salarioVendedor = float(input())
qtdVendas = float(input())

salario = salarioVendedor + (qtdVendas*15)/100

print(f"TOTAL = R$ {salario:.2f}")
"""
"""
linha1 = input().split() #o split pega a string e separa pelo que esta nos parenteses (nesse caso separa pelo espaco) e cria uma lista [item 0, item 1, item n]
a1 = int(linha1[0]) #aqui eu converto essa string que esta na lista para um inteiro
b1 = int(linha1[1])
c1 = float(linha1[2])

linha2 = input().split()
a2 = int(linha2[0])
b2 = int(linha2[1])
c2 = float(linha2[2])

valor = b1*c1 + b2*c2
print(f"VALOR A PAGAR: R$ {valor:.2f}")
"""
