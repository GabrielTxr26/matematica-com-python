# Matemática com Python

Programa em Python, feito para rodar no terminal, com um menu para cálculos de **eletricidade** e **trigonometria**.

Este é o meu primeiro projeto versionado com Git e publicado no GitHub.

## O que o programa faz

- **Eletricidade:** calcula o consumo em kWh e o custo total de um aparelho a partir da potência (W) e das horas de uso.
- **Trigonometria pelos lados:** calcula seno, cosseno ou tangente a partir dos lados de um triângulo retângulo.
- **Trigonometria pelo ângulo:** informa seno, cosseno e tangente de um ângulo em graus.

O programa também valida as entradas: não aceita letras no lugar de números, lados zerados ou negativos, nem cateto maior que a hipotenusa.

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

## Exemplo de uso

```
==============================
     MATEMÁTICA COM PYTHON
==============================
[1] - Eletricidade
[2] - Trigonometria pelos lados
[3] - Trigonometria pelo ângulo
[4] - Sair
Escolha uma opção: 1

===== ELETRICIDADE =====
Digite a potência do aparelho (W): 1000
Digite as horas de uso: 2

Você teve um consumo de 2.00 kWh.
Custo total: R$ 2.40
```

## Observações

- O valor do kWh está definido na constante `TARIFA_KWH`, no início do arquivo `main.py` (R$ 1,20). Altere esse valor para usar a tarifa da sua região.
- Os números podem ser digitados com ponto ou vírgula (`2.5` ou `2,5`).

## Tecnologias

- Python 3
- Git e GitHub

## Autor

Feito por **Gabriel Teixeira Rocha**: [github.com/GabrielTxr26](https://github.com/GabrielTxr26)
