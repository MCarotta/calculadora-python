"""
Calculadora em Python — Operações matemáticas com interface amigável.
"""


def limpar_tela():
    """Limpa a tela para uma experiência mais limpa."""
    import os
    os.system("cls" if os.name == "nt" else "clear")


def ler_numero(prompt: str):
    """Lê um número do usuário com validação. Retorna None se cancelar."""
    while True:
        try:
            entrada = input(prompt).strip().replace(",", ".")
            if not entrada:
                return None
            return float(entrada)
        except ValueError:
            print("   Digite um numero valido (ex: 5 ou 3.14). Tente de novo.\n")


def mostrar_menu():
    """Exibe o menu principal da calculadora."""
    print("  +-----------------------------------------+")
    print("  |         CALCULADORA - OPERACOES          |")
    print("  +-----------------------------------------+")
    print()
    print("    1. Soma           (+)")
    print("    2. Subtracao      (-)")
    print("    3. Multiplicacao  (x)")
    print("    4. Divisao        (/)")
    print("    5. Potencia       (x^y)")
    print("    6. Raiz quadrada  (sqrt)")
    print("    7. Resto (modulo) (%)")
    print()
    print("    0. Sair")
    print()


def calcular(opcao: int, a: float, b: float = None) -> float | None:
    """Executa a operação escolhida. Para raiz, b é ignorado."""
    if opcao == 1:
        return a + b
    if opcao == 2:
        return a - b
    if opcao == 3:
        return a * b
    if opcao == 4:
        if b == 0:
            print("   Nao e possivel dividir por zero.")
            return None
        return a / b
    if opcao == 5:
        return a ** b
    if opcao == 6:
        if a < 0:
            print("   Raiz quadrada de numero negativo nao e real.")
            return None
        return a ** 0.5
    if opcao == 7:
        if b == 0:
            print("   Resto da divisao por zero nao existe.")
            return None
        return a % b
    return None


def simbolo_operacao(opcao: int) -> str:
    """Retorna o simbolo da operacao para exibicao."""
    simbolos = {1: "+", 2: "-", 3: "x", 4: "/", 5: "^", 6: "sqrt", 7: "%"}
    return simbolos.get(opcao, "?")


def executar_calculo(opcao: int) -> bool:
    """
    Pede os operandos, calcula e mostra o resultado.
    Retorna True para continuar, False para sair.
    """
    if opcao == 6:
        a = ler_numero("   Digite o número: ")
        if a is None:
            return True
        b = None
        expressao = f"sqrt({a})"
    else:
        a = ler_numero("   Primeiro número: ")
        if a is None:
            return True
        b = ler_numero("   Segundo número: ")
        if b is None:
            return True
        sim = simbolo_operacao(opcao)
        expressao = f"{a} {sim} {b}"

    resultado = calcular(opcao, a, b)
    if resultado is not None:
        if isinstance(resultado, float) and resultado == int(resultado):
            resultado = int(resultado)
        else:
            resultado = round(resultado, 10)
        print()
        print(f"   → {expressao} = {resultado}")
    print()
    input("   [Enter] para continuar...")
    return True


def main():
    """Loop principal da calculadora."""
    while True:
        limpar_tela()
        mostrar_menu()
        escolha = input("   Escolha uma opção (0–7): ").strip()

        if escolha == "0":
            limpar_tela()
            print("   Ate logo!\n")
            break

        if escolha not in "1234567":
            print("   Opcao invalida. Use um numero de 0 a 7.\n")
            input("   [Enter] para continuar...")
            continue

        opcao = int(escolha)
        limpar_tela()
        print(f"   Operação: {simbolo_operacao(opcao)}\n")
        executar_calculo(opcao)


if __name__ == "__main__":
    main()
