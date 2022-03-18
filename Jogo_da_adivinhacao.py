import random
from time import sleep
import os

i = 0
palpite = 0
x = input("DESEJA INICIAR O PROGRAMA?\nDIGITE [1] PARA NAO OU DIGITE QUALQUER TECLA PARA CONTINUAR: ")

os.system('clear')
sleep(0.1)
print("...")
sleep(0.5)
print("..")
sleep(0.5)
print(".")
sleep(0.5)
os.system('clear')
print("""================== JOGO DA ADIVINHAÇÃO =====================

INSTRUÇÕES:
- VOCÊ TEM QUE ADIVINHAR UM NUMERO ENTRE 1 A 10.000
- QUEM ACERTAR O NUMERO EM MENOS TENTATIVAS GANHA\n    """)

while x != "1":
    d = 1
    i = random.randint(0, 10000)
    
    palpite = int(input("\nQUAL O SEU PALPITE? "))
    
    while palpite != i:
        if palpite < i:
            print("\nO numero aleatorio é maior do que isso")
            d += 1
            palpite = int(input("\nTente novamente: "))
        elif palpite > i:
            print("\nO numero aleatorio é menor do que isso")
            d += 1
            palpite = int(input("\nTente novamente: "))
        else:
            print("\nVOCÊ DIGITOU UM NUMERO INVALIDO - TENTE NOVAMENTE")
            d += 1
            palpite = int(input("\nTente novamente: "))
    print(f"Você acertou em {d} tentativas")
    
    sleep(0.8)
    
    x = input("\nDESEJA REINICIAR O PROGRAMA?\nDIGITE [1] PARA NAO OU DIGITE QUALQUER TECLA PARA CONTINUAR: ")
    
    os.system('clear')
    
    
    
    
