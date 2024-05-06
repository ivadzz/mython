import random as r
import time as t
import os

def lt():
    os.system('cls')


try:
    continuar = 1
    while continuar == 1:
        with open("saldo.txt","r") as f:
            saldostr = f.readline()

        saldo    = int(saldostr)
        print('Seu saldo é de R${:.2f}'.format(saldo))
        continuar = int(input('Deseja continuar?\n1-Sim\n2-Não\n'))
        lt()
        if continuar != 1:
            print('Obrigado por jogar!')
            break

        print('Seu saldo é de R${:.2f}'.format(saldo))
        valor_aposta = float(input('Quanto deseja apostar?\n'))

        if valor_aposta > saldo:
            print('SALDO INSUFICIENTE!\nDeseja depositar algum valor?\n')
            opcao = int(input('1-Sim\n2-Não\n'))
            if opcao == 1:
                valor_deposito = float(input('Quanto deseja depositar?\n'))
                saldo += valor_deposito
                print('Seu novo saldo é R${:.2f}'.format(saldo))
                print('PRESSIONE QUALQUER TECLA PARA CONTINUAR')
                input()
                lt()
                with open("saldo.txt","w") as f:
                    f.write(str('{:.0f}'.format(saldo)))
            elif opcao == 2:
                print('Obrigado por jogar!')
                break
            else:
                print('OPÇÃO INVÁLIDA!')

        elif valor_aposta < 0:
            print('VALOR INVÁLIDO!')

        else:
            print('NÚMEROS DA ROLETA 0->20')
            print('1-BRANCO(0) = x14\n2-PRETO(PARES) = x2\n3-VERMELHO(ÍMPARES) = x2')
            cor_aposta = int(input('Qual cor deseja apostar R${:.2f}?\n'.format(valor_aposta)))
            if cor_aposta not in [1,2,3]:
                print('OPÇÃO INVÁLIDA!')
            else:
                n_sorteado = r.randint(0,20)
                print('Sorteando...')
                t.sleep(1)
                print('O numero sorteado foi: ', end='' )
                print('{}'.format(n_sorteado))
                if n_sorteado == 0:
                    resposta = 1
                elif n_sorteado % 2 == 0:
                    resposta = 2
                else:
                    resposta = 3
                if cor_aposta == resposta:
                    print("Você ganhou!")
                    t.sleep(1)
                    if resposta == 1:
                        saldo-=valor_aposta
                        saldo += (valor_aposta * 14)
                        print('Você ganhou R${:.2f}'.format(valor_aposta*14))
                        print('Seu novo saldo é R${:.2f}'.format(saldo))
                        with open("saldo.txt","w") as f:
                            f.write(str('{:.0f}'.format(saldo)))
                        print('PRESSIONE QUALQUER TECLA PARA CONTINUAR')
                        input()
                        lt()
                        
                    elif resposta == 2:
                        saldo += valor_aposta 
                        print('Você ganhou R${:.2f}'.format(valor_aposta*2))
                        print('Seu novo saldo é R${:.2f}'.format(saldo))
                        with open("saldo.txt","w") as f:
                            f.write(str('{:.0f}'.format(saldo)))
                            print('PRESSIONE QUALQUER TECLA PARA CONTINUAR')
                        input()
                        lt()
                        
                    else:
                        saldo += valor_aposta 
                        print('Você ganhou R${:.2f}'.format(valor_aposta*2))
                        print('Seu novo saldo é R${:.2f}'.format(saldo))
                        with open("saldo.txt","w") as f:
                            f.write(str('{:.0f}'.format(saldo)))
                        print('PRESSIONE QUALQUER TECLA PARA CONTINUAR')
                        input()
                        lt()
                        

                
                else:
                    saldo -= valor_aposta
                    t.sleep(1)
                    print('Você perdeu R${:.2f}'.format(valor_aposta))
                    print('Seu Saldo é de R${:.2f}'.format(saldo))
                    with open("saldo.txt","w") as f:
                        f.write(str('{:.0f}'.format(saldo)))
                    print('PRESSIONE QUALQUER TECLA PARA CONTINUAR')
                    input()
                    lt()
                    
                    

                








except:
    print("FALHA AO TENTAR ACESSAR SEU SALDO!")