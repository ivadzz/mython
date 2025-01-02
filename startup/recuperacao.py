from funcoes import cripto
from funcoes import uncripto
from funcoes import custom_getpass
import getpass
import os
import sys
import msvcrt



def lt():
    os.system('cls')

def attlista():
    with open('listasenha.txt','r')as f:
        listasenha = [line.strip() for line in f.readlines()]
    with open('listalogin.txt','r')as f:
        listalogin = [line.strip() for line in f.readlines()]
    return listasenha,listalogin

try:
    uncripto()

finally:
    lt()
    with open('listasenha.txt','r')as f:
        listasenha = [line.strip() for line in f.readlines()]
    with open('listalogin.txt','r')as f:
        listalogin = [line.strip() for line in f.readlines()]
    cripto()

    continuar = 0

    while continuar == 0:
        opcao = int(input('1-TROCAR SENHA\n2-RECUPERAR SENHA\n3-EXCLUIR CONTA\n4-LISTAR LOGINS\n5-CONFERIR SALDO\n6-ULTIMO DEPOSITO\n7-ULTIMO SAQUE\n'))

        if opcao == 1:
            uncripto() 
            with open('listasenha.txt','r')as f:
                listasenha = [line.strip() for line in f.readlines()]
            with open('listalogin.txt','r')as f:
                listalogin = [line.strip() for line in f.readlines()]
            cripto()
            lt()          
            login_para_senha = input('INFORME O LOGIN QUE GOSTARIA DE TROCAR A SENHA:\n').lower()
            uncripto() 
            with open('listasenha.txt','r')as f:
                listasenha = [line.strip() for line in f.readlines()]
            with open('listalogin.txt','r')as f:
                listalogin = [line.strip() for line in f.readlines()]
            cripto()            
            if login_para_senha in listalogin:
                indice = listalogin.index(login_para_senha)
                print('LOGIN SELECIONADO: {}\n'.format(login_para_senha))
                while True:
                        novasenha = custom_getpass('DIGITE A NOVA SENHA:')
                        if len(novasenha) < 5:
                            lt()
                            print('A SENHA DEVE TER NO MÍNIMO 5 CARACTERES!')
                        elif len(novasenha) > 10:
                            lt()
                            print('A SENHA NÃO DEVE TER MAIS DE 10 CARACTERES!')
                        else:
                            lt()
                            confirmasenha = custom_getpass('DIGITE NOVAMENTE:')
                            
                            if novasenha == confirmasenha:                               
                                break
                            else:
                                lt()
                                print('AS SENHAS NÃO BATEM, TENTE NOVAMENTE.')
                
                # Atualiza a senha na lista
                listasenha[indice] = novasenha
                
                # Salva as senhas atualizadas no arquivo
                uncripto()
                with open('listasenha.txt', 'w') as f:
                    for senha in listasenha:
                        f.write(senha + '\n')
                cripto()
                print('Senha alterada com sucesso!')
            else:
                print('{} NÃO ENCONTRADO NA BASE DE DADOS\n'.format(login_para_senha))

        elif opcao == 2:
            uncripto() 
            with open('listasenha.txt','r')as f:
                listasenha = [line.strip() for line in f.readlines()]
            with open('listalogin.txt','r')as f:
                listalogin = [line.strip() for line in f.readlines()]
            cripto()
            lt()
            login_para_senha = input('INFORME O LOGIN PARA RECUPERAR A SENHA:\n').lower()
            uncripto() 
            with open('listasenha.txt','r')as f:
                listasenha = [line.strip() for line in f.readlines()]
            with open('listalogin.txt','r')as f:
                listalogin = [line.strip() for line in f.readlines()]
            cripto()
            if login_para_senha not in listalogin:
                print('{} NÃO ENCONTRADO NA BASE DE DADOS\n'.format(login_para_senha))
            else:
                indice = listalogin.index(login_para_senha)
                senha_associada = listasenha[indice]
                print('A senha para o login {} é: {}\n'.format(login_para_senha, senha_associada))

        
        elif opcao == 3:
            uncripto() 
            with open('listasenha.txt','r')as f:
                listasenha = [line.strip() for line in f.readlines()]
            with open('listalogin.txt','r')as f:
                listalogin = [line.strip() for line in f.readlines()]
            cripto()
            lt()
            login_para_remover = input('Digite o login que deseja remover: ').lower()

            uncripto() 
            with open('listasenha.txt','r')as f:
                listasenha = [line.strip() for line in f.readlines()]
            with open('listalogin.txt','r')as f:
                listalogin = [line.strip() for line in f.readlines()]
            cripto()

            if login_para_remover in listalogin:
                # Encontra o índice do login na lista
                indice = listalogin.index(login_para_remover)
                
                # Remove o login e a senha correspondentes das listas
                listalogin.pop(indice)
                listasenha.pop(indice)
                
                # Exclui o arquivo de saldo associado ao login
                saldo_arquivo = 'saldo_{}.txt'.format(login_para_remover)
                if os.path.exists(saldo_arquivo):
                    while True:  # Loop para garantir uma resposta válida
                        opcao = input('DESEJA EXCLUIR O ARQUIVO DE SALDO DE {}\nSIM -> s\nNÃO -> n\n'.format(login_para_remover)).lower()
                        
                        if opcao == 's':
                            os.remove(saldo_arquivo)
                            print('Arquivo de saldo {} removido com sucesso.'.format(saldo_arquivo))
                            break  # Sai do loop após uma resposta válida
                        elif opcao == 'n':
                            print('Arquivo mantido.')
                            break  # Sai do loop após uma resposta válida
                        else:
                            print('Opção inválida! Por favor, digite "s" para SIM ou "n" para NÃO.')
                else:
                    print('Arquivo de saldo não encontrado para o login {}.'.format(login_para_remover))

                # Atualiza os arquivos listalogin.txt e listasenha.txt
                with open('listalogin.txt', 'w') as f:
                    for login in listalogin:
                        f.write(login + '\n')
                uncripto()
                with open('listasenha.txt', 'w') as f:
                    for senha in listasenha:
                        f.write(senha + '\n')
                cripto()
                print('Login e senha removidos com sucesso!')
            else:
                print('Login {} não encontrado na base de dados.'.format(login_para_remover))


        elif opcao == 4: 
            uncripto()
            with open('listasenha.txt','r')as f:
                listasenha = [line.strip() for line in f.readlines()]
            with open('listalogin.txt','r')as f:
                listalogin = [line.strip() for line in f.readlines()]
            cripto()
            lt()
            print('LISTA'.center(80,'-'))
            for i in range (len(listalogin)):
                print('{}){}'.format(i+1,listalogin[i]))
            print('LISTA'.center(80,'-')+ '\n')
        
        elif opcao == 5:
            uncripto() 
            with open('listasenha.txt','r')as f:
                listasenha = [line.strip() for line in f.readlines()]
            with open('listalogin.txt','r')as f:
                listalogin = [line.strip() for line in f.readlines()]
            cripto()
            lt()
            login_para_checar_saldo = input('GOSTARIA DE CHECAR O SALDO DE QUAL LOGIN:\n').lower()

            uncripto() 
            with open('listasenha.txt','r')as f:
                listasenha = [line.strip() for line in f.readlines()]
            with open('listalogin.txt','r')as f:
                listalogin = [line.strip() for line in f.readlines()]
            cripto()

            saldo_arquivo = 'saldo_{}.txt'.format(login_para_checar_saldo)
            if os.path.exists(saldo_arquivo):           
                lt()
                if login_para_checar_saldo in listalogin:
                    with open ('saldo_{}.txt'.format(login_para_checar_saldo),'r')as f:
                        saldo = f.readline()
                    saldo = float(saldo)
                    print('O saldo de {} é de R${:.2f}\n'.format(login_para_checar_saldo,saldo))
                else:
                    lt()
                    print('{} NÃO ENCONTRADO NA BASE DE DADOS\n'.format(login_para_checar_saldo))
            else:
                lt()
                print('ARQUIVO DE SALDO DE {} NÃO EXISTE!'.format(login_para_checar_saldo))


        elif opcao == 6:
            lt()
            with open('historico_depositos.txt', 'r') as f:
                linhas = f.readlines()
            if linhas:
                ultima_linha = linhas[-1].strip()  # Remove espaços em branco extras
                print(f'{ultima_linha}\n\n')
            else:
                print('O arquivo está vazio.\n\n')

        
        elif opcao == 7:
            lt()
            with open('historico_saques.txt', 'r') as f:
                linhas = f.readlines()
            if linhas:
                ultima_linha = linhas[-1].strip()  # Remove espaços em branco extras
                print(f'{ultima_linha}\n\n')
            else:
                print('O arquivo está vazio.\n\n')

        else:
            lt()
            print('ATÉ MAIS!'.center(80,'-'))
            continuar = 1