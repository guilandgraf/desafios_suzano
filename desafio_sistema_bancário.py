import textwrap

def menu (): 
    menu = """   
    ======================= MENU ============================ 
    [d] \t Depositar
    [s] \t Sacar
    [e] \t Extrato
    [q] \t Sair
    Digite a opção desejada ==> """
    return input(textwrap.dedent(menu))

# FUNÇÕES SECUNDÁRIAS DEPOSITAR, SACAR E EXTRATO

def depositar(saldo, valor, extrato, /):
    if valor>0:
        saldo += valor
        extrato += f"Depósito: R$ valor{valor:.2f}\n"
        print (f"\n -DEPÓSITO REALIZADO COM SUCESSO! valor R${valor:.2f}--\n")

    else:
        print ("\n--- OPERAÇÃO FALHOU, O VALOR É INVÁLIDO---")

    return (saldo, extrato)

def sacar (*,saldo, valor, extrato, limite, n_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = n_saques >= limite_saques #COMEÇA A CONTAR DO ZERO

    if excedeu_saldo:
        print(f"\n-SALDO INSUFICIENTE") 

    elif excedeu_limite:
        print("\n-VALOR EXCEDE O LIMITE DE SAQUE")

    elif excedeu_saques:
        print ("\nNÚMERO DE SAQUES EXCEDIDOS")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:R$ {valor:.2f}\n"
        n_saques += 1
        print("\n-SAQUE REALIZADO COM SUCESSO-")

    else:
        print("\nO VALOR INFORMADO É INVÁLIDO")

    return saldo, extrato

def exibir_extrato(saldo, extrato):
        print("\n--------EXTRATO--------")
        print(extrato)
        print(f"Saldo:R${saldo:.2f}")
        print("Fim")


# FUNÇÃO PRINCIPAL - PRECISA DAS FUNÇÕES SECUNDÁRIAS DEFINIDAS

def main ():
    
    LIMITE_SAQUES = 3  #As letras maiúsculas definem a variável como uma constante

    saldo = 0
    limite = 500
    extrato = ""
    n_saques = 0

    while True:

        opcao = menu ()

        if opcao == "d":
            valor = float(input ("informe o valor desejado: "))
        
            saldo, extrato = depositar (saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("INFORME O VALOR DESEJADO:"))

            saldo, extrato=sacar(saldo=saldo, valor=valor, extrato=extrato,
                limite=limite, n_saques=n_saques, limite_saques= LIMITE_SAQUES
            ) 

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print ("OBRIGADO POR USAR NOSSO SISTEMA")
            break

        else:
            print("OPÇÃO INVÁLIDA")        
main()


