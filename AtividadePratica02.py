# -*- coding: utf-8 -*-
# ====================================================================
# Atividade Prática 02
# ====================================================================
# --- Exercício 1: Conversor de Moeda ---
print("--- Exercício 1: Conversor de Moeda ---")
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# Cálculo da conversão
valor_dolares = valor_reais / taxa_dolar
valor_euros = valor_reais / taxa_euro
print(f"Valor em Reais: R$ {valor_reais:.2f}")
print(f"Taxa do Dólar: R$ {taxa_dolar}")
print(f"Taxa do Euro: R$ {taxa_euro}")
print("-" * 30)
print(f"Valor convertido em Dólares: US$ {valor_dolares:.2f}")
print(f"Valor convertido em Euros: € {valor_euros:.2f}")
print("\n" + "="*50 + "\n")


# --- Exercício 2: Calculadora de Desconto ---
print("--- Exercício 2: Calculadora de Desconto ---")
nome_produto_desconto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

# Cálculo do desconto
valor_do_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_do_desconto

print(f"Produto: {nome_produto_desconto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto de: {percentual_desconto}%")
print("-" * 30)
print(f"Valor do Desconto: R$ {valor_do_desconto:.2f}")
print(f"Preço Final com Desconto: R$ {preco_final:.2f}")
print("\n" + "="*50 + "\n")


# --- Exercício 3: Calculadora de Média Escolar ---
print("--- Exercício 3: Calculadora de Média Escolar ---")
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

# Cálculo da média
media_escolar = (nota1 + nota2 + nota3) / 3
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print("-" * 30)
print(f"Média Final: {media_escolar:.2f}")
print("\n" + "="*50 + "\n")

# --- Exercício 4: Calculadora de Consumo de Combustível ---
print("--- Exercício 4: Calculadora de Consumo de Combustível ---")
distancia_percorrida_km = 300
combustivel_gasto_litros = 25

# Cálculo do consumo médio
consumo_medio = distancia_percorrida_km / combustivel_gasto_litros
print(f"Distância Percorrida: {distancia_percorrida_km} km")
print(f"Combustível Gasto: {combustivel_gasto_litros} litros")
print("-" * 30)
print(f"Consumo médio do veículo: {consumo_medio:.2f} km/l")
print("\n" + "="*50 + "\n")