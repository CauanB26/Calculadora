operacao = input("Digite a operacao desejada (soma, sub, mult, div): ")
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

if operacao == "soma":
	resultado = float(numero1) + float(numero2)

if operacao == "sub":
	resultado = float(numero1) - float(numero2)

if operacao == "mult":
	resultado = float(numero1) * float(numero2)

if operacao == "div":
	resultado = float(numero1) / float(numero2)

print("O resultado da operação é: %.2f" %resultado)
