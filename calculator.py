#!/usr/bin/env python3
"""
calculadora.py — Calculadora de linha de comando
Suporta operações básicas e avançadas.
"""

import math
import re


def clear_screen():
    print("\033[H\033[J", end="")


def print_banner():
    print("=" * 40)
    print("         🧮  CALCULADORA PYTHON")
    print("=" * 40)


def print_menu():
    print("\nOperações disponíveis:")
    print("  + → Adição")
    print("  - → Subtração")
    print("  * → Multiplicação")
    print("  / → Divisão")
    print("  % → Módulo (resto)")
    print("  ^ → Potência")
    print("  r → Raiz quadrada (un.)")
    print("  l → Logaritmo (base 10)")
    print("  s → Seno  |  c → Cosseno")
    print("  h → Histórico")
    print("  q → Sair")
    print("-" * 40)


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠️  Valor inválido. Digite um número.")


def calculate(op: str, history: list) -> None:
    try:
        # Operações com um único operando
        if op in ("r", "l", "s", "c"):
            a = get_number("  Número: ")
            if op == "r":
                if a < 0:
                    print("  ❌ Não é possível calcular raiz de número negativo.")
                    return
                result = math.sqrt(a)
                expr = f"√{a}"
            elif op == "l":
                if a <= 0:
                    print("  ❌ Logaritmo indefinido para valores ≤ 0.")
                    return
                result = math.log10(a)
                expr = f"log({a})"
            elif op == "s":
                result = math.sin(math.radians(a))
                expr = f"sen({a}°)"
            elif op == "c":
                result = math.cos(math.radians(a))
                expr = f"cos({a}°)"

        # Operações com dois operandos
        else:
            a = get_number("  Primeiro número:  ")
            b = get_number("  Segundo número:   ")

            if op == "+":
                result = a + b
                expr = f"{a} + {b}"
            elif op == "-":
                result = a - b
                expr = f"{a} - {b}"
            elif op == "*":
                result = a * b
                expr = f"{a} × {b}"
            elif op == "/":
                if b == 0:
                    print("  ❌ Divisão por zero não é permitida.")
                    return
                result = a / b
                expr = f"{a} ÷ {b}"
            elif op == "%":
                if b == 0:
                    print("  ❌ Módulo por zero não é permitido.")
                    return
                result = a % b
                expr = f"{a} % {b}"
            elif op == "^":
                result = a ** b
                expr = f"{a} ^ {b}"
            else:
                print("  ⚠️  Operação desconhecida.")
                return

        # Exibe e salva resultado
        print(f"\n  ✅  {expr} = {result}")
        history.append(f"{expr} = {result}")

    except Exception as e:
        print(f"  ❌ Erro inesperado: {e}")


def show_history(history: list) -> None:
    print("\n--- Histórico ---")
    if not history:
        print("  (nenhuma operação realizada)")
    else:
        for i, entry in enumerate(history, 1):
            print(f"  {i}. {entry}")
    print("-----------------")


def main():
    history = []
    valid_ops = {"+", "-", "*", "/", "%", "^", "r", "l", "s", "c"}

    clear_screen()
    print_banner()

    while True:
        print_menu()
        op = input("  Escolha uma operação: ").strip().lower()

        if op == "q":
            print("\n  👋 Até logo!\n")
            break
        elif op == "h":
            show_history(history)
        elif op in valid_ops:
            calculate(op, history)
        else:
            print("  ⚠️  Opção inválida. Tente novamente.")

        input("\n  [Enter para continuar]")
        clear_screen()
        print_banner()


if __name__ == "__main__":
    main()
