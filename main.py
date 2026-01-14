from messages import display_messages
import random
import time

print('Iniciando o projeto 3..2..1')
time.sleep(3)

while True:
    resposta = input('Deseja receber um Conselho? S/N :')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()
