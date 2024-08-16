import os
import time as t
import getpass
import random as r
from cripto import cripto
from cripto import uncripto
from cripto import criptosenha
from cripto import uncriptosenha
import sys
import msvcrt
from colorama import Fore, Back, Style, init


def custom_getpass(prompt="Senha:", char_mask='•'):
    print(prompt, end='', flush=True)
    senha = ""
    while True:
        char = msvcrt.getch()
        if char == b'\r':  # Enter key pressed
            print('')
            break
        elif char == b'\x08':  # Backspace pressed
            if len(senha) > 0:
                senha = senha[:-1]
                sys.stdout.write('\b \b')
        else:
            senha += char.decode('utf-8')
            sys.stdout.write(char_mask)
        sys.stdout.flush()
    return senha


def apresentar_jogos():
    print("=" * 50)
    print("|" + " " * 16 + "SELEÇÃO DE JOGOS" + " " * 16 + "|")
    print("=" * 50)
    print("|" + " " * 48 + "|")
    print("|" + " " * 16 + "1 - ROLETA" + " " * 22 + "|")
    print("|" + " " * 16 + "2 - CAÇA NÍQUEL" + " " * 17 + "|")
    print("|" + " " * 16 + "0 - VOLTAR" + " " * 22 + "|")
    print("|" + " " * 48 + "|")
    print("=" * 50)
    print("\n")


def lt():
    os.system('cls')


try:
    uncripto()


finally:

    with open('listalogin.txt', 'r') as f:
        listalogin = [line.strip() for line in f.readlines()]

    with open('listasenha.txt', 'r') as f:
        listasenha = [line.strip() for line in f.readlines()]

    cripto()
    lt()

    continuar  = 1
    init()
    print('BEM VINDO'.center(80,'-'))
    
    while continuar == 1:
        try:
            opcaologin = int(input('1-Login\n2-Cadastrar\n3-FECHAR\n'))
            if opcaologin == 1:
                lt()
                login = input('Digite seu login:')
                uncripto()
                with open('listasenha.txt','r')as f:
                    listasenha = [line.strip() for line in f.readlines()]
                with open('listalogin.txt','r')as f:
                    listalogin = [line.strip() for line in f.readlines()]
                cripto()
                lt()
                if login not in listalogin:
                    lt()
                    print('LOGIN NÃO ENCONTRADO, FAÇA O CADASTRO.')
                else:
                    senha = custom_getpass()
                    uncripto() 
                    with open('listasenha.txt','r')as f:
                        listasenha = [line.strip() for line in f.readlines()]
                    with open('listalogin.txt','r')as f:
                        listalogin = [line.strip() for line in f.readlines()]
                    cripto()                    
                    index = listalogin.index(login)
                    if senha == listasenha[index]:
                        saldo_file = f'saldo_{login}.txt'
                        lt()
                        try:
                            with open (saldo_file,'r')as f:
                                saldo = f.readline().strip()  # Lê e limpa o saldo
                            saldo = float(saldo)

                        except FileNotFoundError:
                            # Se o arquivo não for encontrado, assume saldo zero e cria o arquivo
                            saldo = '0.00'
                            with open(saldo_file, 'w') as f:
                                f.write(saldo)
                            
                        try:
                            saldo = float(saldo)
                            print('BEM VINDO, '+login + '!')
                            print('Seu saldo é: R${:.2f}'.format(saldo))
                            input('PRESSIONE ENTER PARA CONTINUAR...')
                            continuarr = 0
                            lt()
                                                      
                            saldo = float(saldo)
                            while continuarr == 0:
                                try:
                                    print('{} --> R${:.2f}'.format(login,saldo))
                                    sair = int(input('1-JOGAR\n2-DEPOSITAR\n3-SACAR\n4-SAIR\n'))

                                    if sair == 1:
                                        lt()
                                        continuarjogo = 1                                       
                                        while continuarjogo == 1:
                                            print('{}, seu saldo é de R${:.2f}'.format(login,saldo))
                                            apresentar_jogos()
                                            
                                            try:
                                                opcaojogos=int(input('QUAL JOGO GOSTARIA DE JOGAR:'))

                                                if opcaojogos == 0:
                                                    lt()
                                                    continuarjogo = 0
                                                
                                           
                                                elif opcaojogos == 1:
                                                    lt()
                                                    print('{}, seu saldo é de R${:.2f}\nJOGO SELECIONADO: ROLETA\n'.format(login,saldo))
                                                    try:
                                                        valor_aposta = float(input('Quanto deseja apostar:'))
                                                        if valor_aposta > saldo:
                                                            lt()
                                                            print('SALDO INSUFICIENTE!\nDEPOSITE MAIS!')
                                                            input('PRESSIONE ENTER PARA CONTINUAR...')
                                                            lt()
                                                            continuarjogo = 0

                                                        elif valor_aposta < 1:
                                                            lt()
                                                            print('O VALOR MÍNIMO PARA APOSTAR É DE R$1,00.')
                                                            input('PRESSIONE ENTER PARA CONTINUAR...')
                                                            lt()

                                                        else:
                                                            lt()
                                                            print('NÚMEROS DA ROLETA 0->20')
                                                            print(Fore.GREEN+'1-VERDE(0) = x14\n'+Fore.BLACK+'2-PRETO(PARES) = x2\n'+Fore.RED+'3-VERMELHO(ÍMPARES) = x2'+Fore.WHITE)
                                                            try:
                                                                cor_aposta = int(input('Qual cor deseja apostar R${:.2f}?\n'.format(valor_aposta)))
                                                                if cor_aposta not in [1,2,3]:
                                                                    lt()
                                                                    print('OPÇÃO INVÁLIDA!')
                                                                else:
                                                                    lt()
                                                                    n_sorteado = r.randint(0,20)


                                                                    print('COR SELECIONADA: ',end='')
                                                                    if cor_aposta == 1:
                                                                        print(Fore.GREEN+'VERDE'+Fore.WHITE)
                                                                    elif cor_aposta == 2:
                                                                        print(Fore.BLACK+'PRETO'+Fore.WHITE)
                                                                    else:
                                                                        print(Fore.RED+'VERMELHO'+Fore.WHITE)


                                                                    print('Sorteando...')
                                                                    for j in range(30):
                                                                        nsorteio = r.randint(0,20)
                                                                        print('{}'.format(nsorteio).ljust(2), end='\r', flush=True)
                                                                        t.sleep(.1)

                                                                    if n_sorteado == 0:
                                                                        resposta = 1
                                                                    elif n_sorteado % 2 == 0:
                                                                        resposta = 2
                                                                    else:
                                                                        resposta = 3

                                                                    print('O numero sorteado foi: ',end='' )
                                                                    if resposta == 1:
                                                                        print(Fore.GREEN+'{}'.format(n_sorteado)+Fore.WHITE)
                                                                    elif resposta == 2:
                                                                        print(Fore.BLACK+'{}'.format(n_sorteado)+Fore.WHITE)
                                                                    else:
                                                                        print(Fore.RED+'{}'.format(n_sorteado)+Fore.WHITE)


                                                                    if cor_aposta == resposta:
                                                                        print("Você ganhou!")
                                                                        t.sleep(1)
                                                                        if resposta == 1:
                                                                            saldo-=valor_aposta
                                                                            saldo += (valor_aposta * 14)
                                                                            print('Você ganhou R${:.2f}'.format(valor_aposta*14))
                                                                            print('Seu novo saldo é R${:.2f}'.format(saldo))
                                                                            with open("saldo_{}.txt".format(login),"w") as f:
                                                                                f.write(str('{:.2f}'.format(saldo)))
                                                                            print('PRESSIONE QUALQUER TECLA PARA CONTINUAR')
                                                                            input()
                                                                            lt()
                                                                            
                                                                        elif resposta == 2:
                                                                            saldo += valor_aposta 
                                                                            print('Você ganhou R${:.2f}'.format(valor_aposta*2))
                                                                            print('Seu novo saldo é R${:.2f}'.format(saldo))
                                                                            with open("saldo_{}.txt".format(login),"w") as f:
                                                                                f.write(str('{:.2f}'.format(saldo)))
                                                                                print('PRESSIONE QUALQUER TECLA PARA CONTINUAR')
                                                                            input()
                                                                            lt()
                                                                            
                                                                        else:
                                                                            saldo += valor_aposta 
                                                                            print('Você ganhou R${:.2f}'.format(valor_aposta*2))
                                                                            print('Seu novo saldo é R${:.2f}'.format(saldo))
                                                                            with open("saldo_{}.txt".format(login),"w") as f:
                                                                                f.write(str('{:.2f}'.format(saldo)))
                                                                            print('PRESSIONE QUALQUER TECLA PARA CONTINUAR')
                                                                            input()
                                                                            lt()
                                                                            

                                                                    
                                                                    else:
                                                                        saldo -= valor_aposta
                                                                        t.sleep(1)
                                                                        print('Você perdeu R${:.2f}'.format(valor_aposta))
                                                                        print('Seu Saldo é de R${:.2f}'.format(saldo))
                                                                        with open("saldo_{}.txt".format(login),"w") as f:
                                                                            f.write(str('{:.0f}'.format(saldo)))
                                                                        print('PRESSIONE QUALQUER TECLA PARA CONTINUAR')
                                                                        input()
                                                                        lt()



                                                            
                                                            except ValueError:
                                                                lt()
                                                                print('POR FAVOR, DIGITE UM NÚMERO DE 1 A 3!')
                                                                input('PRESSIONE ENTER PARA CONTINUAR...')
                                                                lt()
                                                        
                                                        
                                                    except ValueError:
                                                        lt()
                                                        print('INFORME O VALOR QUE DESEJA APOSTAR!')


                                                elif opcaojogos == 2:
                                                    lt()
                                                    print('caçaaaaaaaa')
                                                
                                                
                                                else:
                                                    lt()
                                                    print('OPÇÃO INVÁLIDA')
                                                

                                            except ValueError:
                                                lt()
                                                print('SELECIONE UM NÚMERO!')


                                    elif sair == 2:
                                        lt()
                                        uncriptosenha()
                                        with open ('1senhamestre.txt','r')as f:
                                            senhamestre = f.readline().strip()
                                        criptosenha()

                                        try:
                                            valor_deposito = float(input('Quanto deseja depositar?\n'))
                                            if valor_deposito < 1:
                                                lt()
                                                print('VALOR MÍNIMO R$1,00. TENTE NOVAMENTE!')
                                            else:                                   
                                                senhaautorizacao = custom_getpass('Senha de autorização:')
                                                lt()
                                                if senhaautorizacao != senhamestre:
                                                    print('SENHA INCORRETA!\n')
                                                else:
                                                    saldo+=valor_deposito
                                                    with open(f"saldo_{login}.txt", "w") as f:
                                                        f.write('{:.2f}'.format(saldo))
                                                    print('DEPÓSITO DE R${:.2f} REALIZADO COM SUCESSO!'.format(valor_deposito))
                                                    print('Seu novo saldo é R${:.2f}'.format(saldo))
                                                    input('PRESSIONE ENTER PARA CONTINUAR...')
                                                    lt()
                                        except ValueError:
                                            lt()
                                            print('Entrada inválida. Por favor, insira um valor.')
                                        
                                                               
                                    elif sair == 3:
                                        lt()
                                        try:                                  
                                            valor_saque = float(input('{} R${:.2f}\nQUANTO DESEJA SACAR?\n'.format(login,saldo)))
                                            if valor_saque > saldo:
                                                lt()
                                                print('SALDO INSUFICIENTE!')
                                            
                                            elif valor_saque < 50:
                                                lt()
                                                print('O VALOR DO SAQUE DEVE SER DE NO MÍNIMO R$50,00.')

                                            else:
                                                lt()
                                                senha_confirmacao_saque = custom_getpass('DIGITE SUA SENHA:')
                                                if senha_confirmacao_saque == senha:                                              
                                                    saldo -= valor_saque
                                                    lt()
                                                    with open(f"saldo_{login}.txt", "w") as f:
                                                        f.write('{:.2f}'.format(saldo))
                                                    print('SAQUE DE R${:.2f} REALIZADO COM SUCESSO!'.format(valor_saque))
                                                    print('Seu novo saldo é R${:.2f}'.format(saldo))
                                                    input('PRESSIONE ENTER PARA CONTINUAR...')
                                                    lt()
                                                    # Salvar o saldo atualizado no arquivo
                                                
                                                else:
                                                    lt()
                                                    print('SENHA INCORRETA!\n')

                                        except ValueError:
                                            lt()
                                            print('Entrada inválida. Por favor, insira um valor.')


                                    elif sair == 4:
                                        lt()
                                        print('ATÉ MAIS, {}!'.center(80,'-').format(login))
                                        t.sleep(2)
                                        lt()
                                        continuarr = 1 #volta pro inicio

                                    else:
                                        lt()
                                        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
                                        continuarr = 0 #volta pro inicio

                                except ValueError:
                                    lt()
                                    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
                            
                        except ValueError:
                            lt()
                            print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')

                    else:
                        lt()
                        print('SENHA INCORRETA!')
                

            elif opcaologin == 2:

                uncripto()
                with open('listasenha.txt','r')as f:
                    listasenha = [line.strip() for line in f.readlines()]
                with open('listalogin.txt','r')as f:
                    listalogin = [line.strip() for line in f.readlines()]
                cripto()
                lt()

                login = input('CRIE UM LOGIN:')

                uncripto()
                with open('listasenha.txt','r')as f:
                    listasenha = [line.strip() for line in f.readlines()]
                with open('listalogin.txt','r')as f:
                    listalogin = [line.strip() for line in f.readlines()]
                cripto()
                
                if login in listalogin or login.strip()=='':
                    lt()
                    print('LOGIN INDISPONÍVEL! TENTE OUTRO!')
                # Após sair do loop, temos um login único
                
                else:
                    while True:
                        senha = custom_getpass('CRIE UMA SENHA:')
                        if len(senha) < 5:
                            lt()
                            print('A SENHA DEVE TER NO MÍNIMO 5 CARACTERES!')
                        elif len(senha) > 10:
                            lt()
                            print('A SENHA NÃO DEVE TER MAIS DE 10 CARACTERES!')
                        else:
                            lt()
                            confirmasenha = custom_getpass('DIGITE NOVAMENTE:')
                            
                            if senha == confirmasenha:                               
                                break
                            else:
                                lt()
                                print('AS SENHAS NÃO BATEM, TENTE NOVAMENTE.')


                    uncripto()
                    listalogin.append(login)  # Adiciona o novo login à lista
                    with open('listalogin.txt', 'a') as f:
                        f.write(login + '\n')  # Adiciona o login e uma nova linha
                        
                    listasenha.append(senha)
                    with open('listasenha.txt','a') as f:
                        f.write(senha + '\n')
                    cripto()
                    print('CONTA CRIADA COM SUCESSO!')
                    t.sleep(2)
                    lt()


            elif opcaologin == 3:
                continuar = 0


            else:
                lt()
                continuar = 1


        except ValueError:
            lt()
            print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
