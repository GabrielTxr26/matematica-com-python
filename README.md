# Matemática com Python

Programa em Python, feito para rodar no terminal, com um menu para cálculos de **eletricidade**, **trigonometria** e **equação do 2º grau**.

Este é o meu primeiro projeto versionado com Git e publicado no GitHub.

## O que o programa faz

- **Eletricidade:** calcula o consumo em kWh e o custo total de um aparelho a partir da potência (W) e das horas de uso.
- **Trigonometria pelos lados:** calcula seno, cosseno ou tangente a partir dos lados de um triângulo retângulo.
- **Trigonometria pelo ângulo:** informa seno, cosseno e tangente de um ângulo em graus.
- **Equação do 2º grau (Bhaskara):** calcula o delta e as raízes reais de uma equação `ax² + bx + c = 0`.

O programa também valida as entradas: não aceita letras no lugar de números, lados zerados ou negativos, cateto maior que a hipotenusa, nem `a = 0` na equação do 2º grau.

## Como rodar

Você precisa ter o [Python 3](https://www.python.org/downloads/) instalado.

1. Baixe ou clone o repositório:

```
   git clone https://github.com/GabrielTxr26/matematica-com-python.git
```

2. Entre na pasta do projeto:

```
   cd matematica-com-python
```

3. Execute o programa:

```
   python main.py
```

## Exemplos de uso

### Eletricidade

```
==============================
     MATEMÁTICA COM PYTHON
==============================
[1] - Eletricidade
[2] - Trigonometria pelos lados
[3] - Trigonometria pelo ângulo
[4] - Equação do 2º grau
[5] - Sair
Escolha uma opção: 1

===== ELETRICIDADE =====
Digite a potência do aparelho (W): 1000
Digite as horas de uso: 2

Você teve um consumo de 2.00 kWh.
Custo total: R$ 2.40
```

### Equação do 2º grau

```
Escolha uma opção: 4

===== EQUAÇÃO DO 2º GRAU =====
Formato: ax² + bx + c = 0
Digite o valor de a: 1
Digite o valor de b: -5
Digite o valor de c: 6

Delta: 1.00
Duas raízes reais: x1 = 3.00 e x2 = 2.00
```

## Observações

- O valor do kWh está definido na constante `TARIFA_KWH`, no início do arquivo `main.py` (R$ 1,20). Altere esse valor para usar a tarifa da sua região.
- Os números podem ser digitados com ponto ou vírgula (`2.5` ou `2,5`).

## Tecnologias

- Python 3
- Git e GitHub

## Autor

Feito por **Gabriel Teixeira Rocha**: [github.com/GabrielTxr26](https://github.com/GabrielTxr26)
