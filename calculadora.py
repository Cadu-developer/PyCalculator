import math
from flask import render_template, request

def calcular():

    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    resultado = ""
    etapas = ""

    # RAIZ QUADRADA
    if operacao == "sqrt":

        if num1 < 0:
            resultado = "Erro"
            etapas = f"Não existe raiz real de {int(num1)}"

        else:
            resultado = math.sqrt(int(num1))
            etapas = f"√{int(num1)} = {int(resultado)}"

    # LOGARITMO
    elif operacao == "log":

        if num1 <= 0:
            resultado = "Erro"
            etapas = "Logaritmo só existe para números positivos."

        else:
            resultado = math.log10(int(num1))
            etapas = f"log({int(num1)}) = {int(resultado)}"

    # BHASKARA
    elif operacao == "bhaskara":

        a = num1

        b_valor = request.form.get("num2", "").strip()
        c_valor = request.form.get("num3", "").strip()

        if not b_valor or not c_valor:

            return render_template(
                "calculadora.html",
                etapas="Digite os valores de B e C",
                resultados=""
            )

        b = float(int(b_valor))
        c = float(int(c_valor))

        delta = (b ** 2) - (4 * a * c)

        if delta < 0:

            resultado = "Erro"

            etapas = (
                f"Δ = {int(delta)}. "
                f"Não existem raízes reais."
            )

        else:

            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)

            resultado = f"x1 = {x1} | x2 = {x2}"

            etapas = (
                f"Δ = {b}² - 4·{a}·{c} = {delta}\n"
                f"x1 = (-{b} + √{delta}) / (2·{a})\n"
                f"x2 = (-{b} - √{delta}) / (2·{a})"
            )

    else:

        num2_valor = request.form.get("num2", "").strip()

        if not num2_valor:

            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número.",
                resultados=""
            )

        num2 = float(num2_valor)

        # Soma
        if operacao == "+":
            resultado = int(num1 + num2)
            etapas = f"{int(num1)} + {int(num2)} = {int(resultado)}"

        # Subtração
        elif operacao == "-":
            resultado = int(num1 - num2)
            etapas = f"{int(num1)} - {int(num2)} = {int(resultado)}"

        # Multiplicação
        elif operacao == "*":
            resultado = int(num1 * num2)
            etapas = f"{int(num1)} * {int(num2)} = {int(resultado)}"

        # Divisão
        elif operacao == "/":

            if num2 == 0:
                resultado = "Erro"
                etapas = "Não existe divisão por zero."

            else:
                resultado = int(num1 / num2)
                etapas = f"{int(num1)} / {int(num2)} = {int(resultado)}"

        # Potência
        elif operacao == "**":
            resultado = num1 ** num2
            etapas = f"{int(num1)} ^ {int(num2)} = {int(resultado)}"

    return render_template(
        "calculadora.html",
        etapas=etapas,
        resultados=resultado
    )