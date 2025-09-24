import textwrap
 
 
def menu (): 
    menu = """   
    ======================= MENU ============================ 
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [q]  Sair
    [nu] Novo usuário
    [lc] Listar contas
    [nc] Nova conta
    \n    DIGITE A OPÇÃO DESEJADA ==> """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor>0:
        saldo += valor
        extrato += f"Depósito: R$ valor{valor:.2f}\n"
        print (f"\n\t---DEPÓSITO REALIZADO COM SUCESSO!\n\t---VALOR DEPOSITADO R${valor:.2f}---\n")
    else:
        print ("\n--- OPERAÇÃO FALHOU, O VALOR É INVÁLIDO---")

    return (saldo, extrato)

def sacar (*,saldo, valor, extrato, limite, n_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = n_saques >= limite_saques #COMEÇA A CONTAR DO ZERO

    if excedeu_saldo:
        print(f"\n\t---SALDO INSUFICIENTE---") 

    elif excedeu_limite:
        print("\n\t---VALOR EXCEDE O LIMITE DE SAQUE---")

    elif excedeu_saques:
        print ("\n\t---NÚMERO DE SAQUES EXCEDIDOS---")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:R$ {valor:.2f}\n"
        n_saques += 1
        print("\n\t---SAQUE REALIZADO COM SUCESSO---")

    else:
        print("\n\t---O VALOR INFORMADO É INVÁLIDO---")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
        print("\n--------EXTRATO--------")
        print(extrato)
        print(f"Saldo:R${saldo:.2f}")
        print("Fim")

def criar_usuario(usuarios):

    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n !!!CPF JÁ CADASTRADO!!!")
        return

    nome=input("nome completo: ")
    data_nasc=input("data_de_nascimento (dd-mm-aaaa): ")
    endereco=input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
   
    usuarios.append({"nome":nome, "data_de_nascimento":data_nasc, "cpf": cpf, "endereco":endereco})

    print ("\n\t\t----USUÁRIO CRIADO COM SUCESSO----")
    
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n--CONTA CRIADA COM SUCESSO!--")
        return {"agencia":agencia, "C/C": numero_conta, "usuario": usuario}
    
    print("\n--USUÁRIO NÃO EXISTENTE--\n--POR FAVOR, CRIE UM USUÁRIO--")

def listar_contas (contas): 
    for conta in contas:

        linha = f"""\
            Agência:\t{conta['agencia']}
            C\C:\t{conta['C/C']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main ():

    AGENCIA = "0001"
    LIMITE_SAQUES = 3  

    saldo = 0
    limite = 500
    extrato = ""
    n_saques = 0
    usuarios = []
    contas = []
   

    while True:

        opcao = menu ()

        if opcao == "d":
            valor = float(input ("informe o valor desejado: "))
        
            saldo, extrato = depositar (saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("INFORME O VALOR DESEJADO:"))

            saldo, extrato=sacar(saldo=saldo, valor=valor, extrato=extrato,
                limite=limite, n_saques=n_saques, limite_saques= LIMITE_SAQUES)
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print ("\n\t---OBRIGADO POR USAR NOSSO SISTEMA---\n")
            break

        else:
            print("OPÇÃO INVÁLIDA")       

main()
