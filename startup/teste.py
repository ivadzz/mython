import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_baralho():
    baralho = []
    naipes = ['Copas', 'Ouros', 'Espadas', 'Paus']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    for naipe in naipes:
        for valor in valores:
            baralho.append((valor, naipe))
    
    random.shuffle(baralho)
    return baralho

def calcular_pontuacao(mao):
    valor_total = 0
    ases = 0
    
    for carta in mao:
        valor, _ = carta
        if valor in ['J', 'Q', 'K']:
            valor_total += 10
        elif valor == 'A':
            ases += 1
            valor_total += 11
        else:
            valor_total += int(valor)
    
    while valor_total > 21 and ases:
        valor_total -= 10
        ases -= 1
    
    return valor_total

def mostrar_mao(mao, jogador=True):
    if jogador:
        print("Sua mão:")
    else:
        print("Mão do Dealer:")
    
    for carta in mao:
        print(f'{carta[0]} de {carta[1]}')
    print(f"Pontuação: {calcular_pontuacao(mao)}\n")

def blackjack():
    limpar_tela()
    print("Bem-vindo ao Blackjack!\n")
    
    baralho = criar_baralho()
    
    mao_jogador = [baralho.pop(), baralho.pop()]
    mao_dealer = [baralho.pop(), baralho.pop()]
    
    mostrar_mao(mao_jogador)
    
    while calcular_pontuacao(mao_jogador) < 21:
        acao = input("Deseja 'h' para hit (mais uma carta) ou 's' para stand (parar): ").lower()
        if acao == 'h':
            mao_jogador.append(baralho.pop())
            mostrar_mao(mao_jogador)
        elif acao == 's':
            break
        else:
            print("Opção inválida, por favor escolha 'h' para hit ou 's' para stand.")
    
    while calcular_pontuacao(mao_dealer) < 17:
        mao_dealer.append(baralho.pop())
    
    mostrar_mao(mao_dealer, jogador=False)
    
    pontuacao_jogador = calcular_pontuacao(mao_jogador)
    pontuacao_dealer = calcular_pontuacao(mao_dealer)
    
    if pontuacao_jogador > 21:
        print("Você estourou! Dealer vence.")
    elif pontuacao_dealer > 21 or pontuacao_jogador > pontuacao_dealer:
        print("Parabéns, você venceu!")
    elif pontuacao_jogador == pontuacao_dealer:
        print("Empate!")
    else:
        print("Dealer vence!")
    
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente == 's':
        blackjack()
    else:
        print("Obrigado por jogar!")

if __name__ == "__main__":
    blackjack()
