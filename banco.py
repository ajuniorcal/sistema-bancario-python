def menu():
    print("""
==============================
        BANCO PYTHON
==============================
[1] Criar conta
[2] Depositar
[3] Sacar
[4] Extrato
[5] Listar contas
[0] Sair
==============================""")
    return input("=> Escolha uma opção: ")


def criar_conta(contas):
    nome = input("Informe o nome do titular: ")
    cpf = input("Informe o CPF do titular: ")
    conta_id = len(contas) + 1
    conta = {
        "id": conta_id,
        "titular": nome,
        "cpf": cpf,
        "saldo": 0.0,
        "extrato": "",
        "saques": 0
    }
    contas.append(conta)
    print(f"\n✅ Conta criada com sucesso! Número da conta: {conta_id}")
    return conta


def buscar_conta(contas, cpf):
    for conta in contas:
        if conta["cpf"] == cpf:
            return conta
    return None


def depositar(contas):
    cpf = input("Informe o CPF do titular: ")
    conta = buscar_conta(contas, cpf)

    if not conta:
        print("\n❌ Conta não encontrada.")
        return

    valor = float(input("Informe o valor do depósito: R$ "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("❌ Valor inválido. O depósito deve ser positivo.")


def sacar(contas):
    LIMITE_SAQUE = 3
    LIMITE_VALOR = 500.0

    cpf = input("Informe o CPF do titular: ")
    conta = buscar_conta(contas, cpf)

    if not conta:
        print("\n❌ Conta não encontrada.")
        return

    valor = float(input("Informe o valor do saque: R$ "))

    if valor <= 0:
        print("\n❌ Valor inválido.")
    elif valor > conta["saldo"]:
        print("\n❌ Saldo insuficiente.")
    elif valor > LIMITE_VALOR:
        print("\n❌ O limite máximo por saque é de R$ 500.")
    elif conta["saques"] >= LIMITE_SAQUE:
        print("\n❌ Limite de saques diários atingido.")
    else:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque:    R$ {valor:.2f}\n"
        conta["saques"] += 1
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")


def extrato(contas):
    cpf = input("Informe o CPF do titular: ")
    conta = buscar_conta(contas, cpf)

    if not conta:
        print("\n❌ Conta não encontrada.")
        return

    print("\n========== EXTRATO ==========")
    print(conta["extrato"] if conta["extrato"] else "Nenhuma movimentação realizada.")
    print(f"\nSaldo atual: R$ {conta['saldo']:.2f}")
    print("=============================")


def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada ainda.")
        return

    print("\n======= LISTA DE CONTAS =======")
    for conta in contas:
        print(f"Conta: {conta['id']} | Titular: {conta['titular']} | CPF: {conta['cpf']} | Saldo: R$ {conta['saldo']:.2f}")
    print("================================")


def main():
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            criar_conta(contas)
        elif opcao == "2":
            depositar(contas)
        elif opcao == "3":
            sacar(contas)
        elif opcao == "4":
            extrato(contas)
        elif opcao == "5":
            listar_contas(contas)
        elif opcao == "0":
            print("\n👋 Obrigado por usar o Banco Python! Até logo.")
            break
        else:
            print("\n❌ Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
