menu = """
[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair
=> """

saldo = 0
limite = 500
extrato = ""
deposito = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor: .2f}\n"

        else:
            print("Operação falhou! O valor informado é invalido.")
    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! o valor do saque excede o limite.")
        
        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! o valor informado é invalido.")
    
    elif opcao == "2":
        print("\n==================== Extrato ====================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================================")
    
    elif opcao == "3" :
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
