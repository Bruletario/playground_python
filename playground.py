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
"""
raio = float(input())
pi = 3.14159
calc_volume = (4.0/3.0)*pi*raio**3

print(f"VOLUME = {calc_volume:.3f}")
"""
"""
linha = input().split()

val1 = float(linha[0])
val2 = float(linha[1])
val3 = float(linha[2])

pi = 3.14159

areaT = (val1*val3)/2
areaC = pi*val3**2
areaTz = ((val1+val2)*val3)/2
areaQ = val2**2
areaR = val1*val2

print(f"TRIANGULO: {areaT:.3f}")
print(f"CIRCULO: {areaC:.3f}")
print(f"TRAPEZIO: {areaTz:.3f}")
print(f"QUADRADO: {areaQ:.3f}")
print(f"RETANGULO: {areaR:.3f}")
"""
"""
linha = input().split()

val1 = int(linha[0])
val2 = int(linha[1])
val3 = int(linha[2])

maiorAb = (val1+val2+abs(val1-val2))/2 #nesse caso abs() quer dizer absolute, ou seja a operacao modulo da conta
maiorBc = int((maiorAb+val3+abs(maiorAb-val3))/2)

print(f"{maiorBc} eh o maior")
"""
"""
distancia = int(input())
combustivelGasto = float(input())

consumoMedio = distancia/combustivelGasto

print(f"{consumoMedio:.3f} km/l")
"""
"""
linha1 = input().split()
linha2 = input().split()

coordx1 = float(linha1[0])
coordx2 = float(linha2[0])

coordy1 = float(linha1[1])
coordy2 = float(linha2[1])

distancia = ((coordx2-coordx1)**2+(coordy2-coordy1)**2)**(1/2)

print(f"{distancia:.4f}")
"""
diferencaKm = int(input())
tempo = 60

quilometrosMin = diferencaKm/tempo

tempoDistancia = diferencaKm/quilometrosMin


print(f"{tempoDistancia} minutos")