from messages import display_messages
import random
import time

print('Iniciando o projeto')
time.sleep(3)

login_username = [
    'Rafael',
    'Luiz',
    'Joao'
]

username = input('usuario para login: ')

while True:
    
    while(username not in login_username):
        print()
        print('Usuario invalido! Tente novamente! ')
        username = input('usuario para login: ')

    resposta = input('Deseja receber um Conselho? S/N :')
    if (resposta == 'S' or resposta == 's'):
        print()
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()
