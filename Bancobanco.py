# Criando um sistema bancário simples com Python

menu = """
###################### B A N C O  B A N C O ######################\n
[d] = Depósito
[s] = Saque
[e] = Extrato
[q] = Sair

=> Escolha uma opção: """

# Definindo as variáveis utilizadas no menu (saldo, depósitos, saques, limites e restrições de uso)
saldo = 0
sum_depositos = 0
sum_saques = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Implementando as condições do sistema
# Módulo de "Enquanto", para retornar o print do menu.
while True:

    opcao = input(menu)

    # Situação de Depósito 
    if opcao == "d":
        #Use um bloco de tentativas, para que o usuário não digite um valor que não seja conversível em float.
            try:
                    valor = float(input("\n Informe o valor do deposito: "))

                    if valor > 0:
                        saldo += valor
                        sum_depositos += valor
                        extrato += f"Deposito: {valor:.2f}\n"
                        print("\n Operação realizada com sucesso!")
                    
                    else:
                        print("\n Operação inválida! Verifique o valor do depósqito.")
            
            except:
                    #Se o usuário digitar um valor inválido, o sistema irá informar
                    print("\n Operação inválida! Verifique o formato informado.")
    # Situação de Saque
    elif opcao == "s":
            #Use um bloco de tentativas, para que o usuário não digite um valor que não seja conversível em float.
            try: 
                    valor = float(input("Informe o valor do saque: "))
                    excedeu_saldo = valor > saldo
                    excedeu_limite = valor > limite
                    excedeu_saques = numero_saques >= LIMITE_SAQUES
                
                    if excedeu_saldo or excedeu_limite or excedeu_saques:
                            print("\n Operação inválida! Verifique o valor do saque ou limite de saques.")

                    elif valor > 0:
                            saldo -= valor
                            sum_saques += valor
                            extrato += f"Saque: {valor:.2f}\n"
                            numero_saques += 1
                            print("\n Saque realizado com sucesso!")
                    
                    else:
                            print("\n Operação inválida! Verifique o valor do saque.")
            except:
                        #Se o usuário digitar um valor inválido, o sistema irá informar
                        print("\n Operação inválida! Verifique o formato informado.")
    # Situação de Extrato
    elif opcao == "e":
        print("\n###################### E X T R A T O ######################\n")
        print("Não ocorreram movimentações na conta.\n")\
            if extrato == "" \
            else print(f"Extrato:\n{extrato}\nDepósitos:{sum_depositos:.2f}\nSaques: -{sum_saques:.2f}\nSaldo: {saldo:.2f}\n")
        print("Banco Banco, o banco mais banco que o seu último banco.\
              \n############################################################\n")
    # Situação de encerramento do sistema
    elif opcao == "q":
        print("Sistema encerrado. Obrigado por utilizar o Banco Banco")
        break
    # Casos não previstos ou erros de digitação
    else:
        print("Opção não encontrada. Verifique a opção desejada.")
        opcao
