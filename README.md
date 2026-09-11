# Cálculo de Fatorial em Python 🐍

Programa simples em Python que calcula o fatorial de um número inteiro utilizando um loop `for`.

## 📋 Descrição

O fatorial de um número `n` (representado por `n!`) é o produto de todos os inteiros positivos menores ou iguais a `n`. Por exemplo:

5! = 5 × 4 × 3 × 2 × 1 = 120


Este programa implementa esse cálculo através da função `calcular`, que recebe um número inteiro e retorna o valor do seu fatorial.

## 🗂️ Estrutura do Código

- **Função `calcular(numero)`**
  - Recebe um número inteiro como parâmetro.
  - Inicializa a variável `resultado` em `1`.
  - Percorre um loop de `1` até `numero`, multiplicando `resultado` a cada iteração.
  - Retorna o valor final do fatorial.
- **Bloco Principal (`__main__`)**
  - Define o número escolhido (`numero_escolhido = 5`).
  - Chama a função `calcular` para obter o resultado.
  - Exibe o resultado no console.

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado.

2. Execute o programa diretamente pelo terminal:
   ```bash
   python calculo_fatorial.py
💻 Saída Esperada
O fatorial de 5 é: 120

## ⚙️ Personalizando
Para calcular o fatorial de outro número, basta alterar o valor da variável numero_escolhido no bloco principal do arquivo:
numero_escolhido = 7  # Altere para o número desejado