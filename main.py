import math

TARIFA_KWH = 1.20  # valor do kWh em reais


def ler_numero(mensagem):
    """Pede um número ao usuário e repete até ele digitar um valor válido."""
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite apenas números!")


def eletricidade():
    print("\n===== ELETRICIDADE =====")

    potencia = ler_numero("Digite a potência do aparelho (W): ")
    horas = ler_numero("Digite as horas de uso: ")

    if potencia < 0 or horas < 0:
        print("Os valores não podem ser negativos!")
        return

    kwh = (potencia * horas) / 1000
    custo_total = kwh * TARIFA_KWH

    print(f"\nVocê teve um consumo de {kwh:.2f} kWh.")
    print(f"Custo total: R$ {custo_total:.2f}")


def trigonometria():
    print("\n===== TRIGONOMETRIA =====")
    print("[1] - Seno")
    print("[2] - Cosseno")
    print("[3] - Tangente")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números!")
        return

    if opcao == 1:
        oposto = ler_numero("Digite o cateto oposto: ")
        hipotenusa = ler_numero("Digite a hipotenusa: ")

        if hipotenusa <= 0 or oposto < 0:
            print("Os lados devem ser maiores que zero!")
        elif oposto > hipotenusa:
            print("O cateto não pode ser maior que a hipotenusa!")
        else:
            seno = oposto / hipotenusa
            print(f"O seno é: {seno:.2f}")

    elif opcao == 2:
        adjacente = ler_numero("Digite o cateto adjacente: ")
        hipotenusa = ler_numero("Digite a hipotenusa: ")

        if hipotenusa <= 0 or adjacente < 0:
            print("Os lados devem ser maiores que zero!")
        elif adjacente > hipotenusa:
            print("O cateto não pode ser maior que a hipotenusa!")
        else:
            cosseno = adjacente / hipotenusa
            print(f"O cosseno é: {cosseno:.2f}")

    elif opcao == 3:
        oposto = ler_numero("Digite o cateto oposto: ")
        adjacente = ler_numero("Digite o cateto adjacente: ")

        if adjacente <= 0 or oposto < 0:
            print("Os catetos devem ser maiores que zero!")
        else:
            tangente = oposto / adjacente
            print(f"A tangente é: {tangente:.2f}")

    else:
        print("Essa opção não existe!")


def trigonometria_por_angulo():
    print("\n===== TRIGONOMETRIA POR ÂNGULO =====")

    angulo = ler_numero("Digite o ângulo em graus: ")

    # Converte graus para radianos
    radianos = math.radians(angulo)

    seno = math.sin(radianos)
    cosseno = math.cos(radianos)

    print(f"\nSeno: {seno:.4f}")
    print(f"Cosseno: {cosseno:.4f}")

    # A tangente não existe quando o cosseno é zero (90°, 270°...)
    if abs(cosseno) < 1e-10:
        print("Tangente: indefinida")
    else:
        tangente = math.tan(radianos)
        print(f"Tangente: {tangente:.4f}")


def bhaskara():
    print("\n===== BHASKARA =====")

    a = ler_numero("Digite o valor de a: ")
    b = ler_numero("Digite o valor de b: ")
    c = ler_numero("Digite o valor de c: ")

    if a == 0:
        print("O valor de 'a' não pode ser zero!")
        return

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Existe uma raiz real: x = {x:.2f}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Existem duas raízes reais: x1 = {x1:.2f}, x2 = {x2:.2f}")


def menu():
    while True:
        print("\n==============================")
        print("     MATEMÁTICA COM PYTHON")
        print("==============================")
        print("[1] - Eletricidade")
        print("[2] - Trigonometria pelos lados")
        print("[3] - Trigonometria pelo ângulo")
        print("[4] - Bhaskara")
        print("[5] - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == 1:
            eletricidade()

        elif opcao == 2:
            trigonometria()

        elif opcao == 3:
            trigonometria_por_angulo()

        elif opcao == 4:
            bhaskara()

        elif opcao == 5:
            print("Programa encerrado!")
            break

        else:
            print("Essa opção não existe!")


if __name__ == "__main__":
    menu()