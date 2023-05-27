saldo = 0
depositos = []
saques = []

while True:
	print("\n===== Menu =====")
	print("1. Depositar")
	print("2. Sacar")
	print("3. Extrato")
	print("0. Sair")
	opcao = input("Digite a opção desejada: ")

	if opcao == "1":
		valor = float(input("Digite o valor a ser depositado: "))
		if valor > 0:
			saldo += valor
			depositos.append(valor)
			print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
		else:
			print("Valor inválido. O depósito deve ser positivo.")
	elif opcao == "2":
		valor = float(input("Digite o valor a ser sacado: "))
		if saldo >= valor and valor <= 500 and len(saques) < 3:
			saldo -= valor
			saques.append(valor)
			print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
		elif saldo < valor:
			print("Saldo insuficiente. Não é possível sacar o valor solicitado.")
		elif valor > 500:
			print("Limite máximo de saque é de R$ 500.00 por operação.")
		elif len(saques) >= 3:
			print("Limite máximo de 3 saques diários atingido.")
	elif opcao == "3":
		if len(depositos) == 0 and len(saques) == 0:
			print("Não foram realizadas movimentações.")
		else:
			print("Extrato:")
			for deposito in depositos:
				print(f"Depósito: R$ {deposito:.2f}")
			for saque in saques:
				print(f"Saque: R$ {saque:.2f}")
			print(f"Saldo atual: R$ {saldo:.2f}")
	elif opcao == "0":
		print("Saindo do sistema...")
		break
	else:
		print("Opção inválida. Digite novamente.")
