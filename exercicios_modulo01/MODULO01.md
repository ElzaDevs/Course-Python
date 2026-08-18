<h1>MODULO 01 FUNDAMENTOS <h1>


## variáveis
 A variável é uma etiqueta apontando para um valor na memória, são tipos de contâiners(nome em caixas). 
 ´´´
 nome = "Ana"         # str  (texto)
 idade = 20           # int  (inteiro)
 altura = 1.68        # float (decimal)
 matriculado = True   # bool  (True/False)
 nada = None      # NoneType ausência de valor)
 ´´´
 ## As regras de nome são que podem possuir letras, números e _ , porém, jamais iniciar com número.


 ## Tipos e conversão 
 type(10)          # <class 'int'>
 int("42")         # 42
 int(3.9)          # 3  (trunca, não arredonda)
 float("3.14")     # 3.14
 str(2026)         # "2026"
 bool(0)           # False
 round(3.567, 2)   # 3.57
---
## ENTRADA E SAIDA
Input() sempre devolverá textos (str), para estar calculando, utilizando ele, converta os dados.
´´´
EXEMPLO: studio_ghibli = float(input("Nota: "))
´´´
---
## Operadores
Temos disponíveis: 
# Aritméticos
Multiplicação(*), Adição(+), Divisão inteira (//), Divisão real(/), Divisão Restos (%).
# Atribuição
Servem para atribuir um valor á outro.
 ´´´
 = += -= *= /= //= **=
´´´
# Comparação
´´´
==(igual) , !=(oposto,negação) , (maior)>, <(menor) , >=(maior igual a), <=(menor igual a).

´´´
# Lógicos(boolean) (v(1))or(f(0))
AND OR NOT
# Pertinência
in, not in 
Muito usado dentro da estrutura repetição "for-para".
# Identidade
is, is not 
---
## Módulo MATH E NUMBERS
  import math
math.sqrt(16)      # 4.0
math.pi            # 3.141592653589793
math.ceil(4.1)     # 5  (arredonda para cima)
math.floor(4.9)    # 4  (para baixo)
math.fabs(-3)      # 3.0
abs(-7)            # 7
max(3, 9, 1)       # 9
min(3, 9, 1)       # 1

---
### EXERCICIES 
1. **IMC**: leia peso e altura e mostre o IMC com 2 casas decimais.
2. **Troco**: leia valor da compra e valor pago; mostre o troco formatado como `R$ 12,50`.
3. **Segundos**: leia uma quantidade de segundos e converta para `h:min:s`.
4. **Média ponderada**: 3 notas com pesos 2, 3 e 5; mostre a média com 1 casa decimal.
5. **Trocar valores**: leia dois números e imprima-os trocados, sem usar variável auxiliar.

-GABARITO ABAIXO- FAÇAM PRIMEIRO A ATIVIDADE!!!!!-
---



## GABARITO:
# 1) IMC
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / altura ** 2
print(f"IMC = {imc:.2f}")

# 2) Troco
compra = float(input("Compra: "))
pago = float(input("Pago: "))
troco = pago - compra
print(f"Troco: R$ {troco:.2f}".replace(".", ","))

# 3) Segundos
total = int(input("Segundos: "))
h = total // 3600
m = (total % 3600) // 60
s = total % 60
print(f"{h:02d}:{m:02d}:{s:02d}")

# 4) Média ponderada
n1 = float(input("Nota 1: ")); n2 = float(input("Nota 2: ")); n3 = float(input("Nota 3: "))
media = (n1 * 2 + n2 * 3 + n3 * 5) / 10
print(f"Média = {media:.1f}")

# 5) Troca
a = input("A: "); b = input("B: ")
a, b = b, a
print(a, b)

