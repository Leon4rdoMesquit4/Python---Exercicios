import random
from time import sleep
import os

x = input("DESEJA INICIAR O PROGRAMA?\nDIGITE [1] PARA NAO OU DIGITE QUALQUER TECLA PARA CONTINUAR: ")

while x != "1":
    os.system('clear')
    sleep(0.1)
    print("...")
    sleep(0.5)
    print("..")
    sleep(0.5)
    print(".")
    sleep(0.5)
    os.system('clear')
    i = int(input("""==================== GERADOR DE DADO =========================
ESCOLHA O DADO A SUA ESCOLHA:
[1] D2
[2] D4
[3] D6
[4] D10
[5] D20
[6] D100 

DIGITE O VALOR AQUI: """))
    
    if i == 1:
        print(f"Seu resultado do D2 é {random.randint(1, 2)}")
    elif i == 2:
        print(f"Seu resultado do D4 é {random.randint(1, 4)}")
    elif i == 3:
        print(f"Seu resultado do D6 é {random.randint(1, 6)}")
    elif i == 4:
        print(f"Seu resultado do D10 é {random.randint(1, 10)}")
    elif i == 5:
        print(f"Seu resultado do D20 é {random.randint(1, 20)}")
    elif i == 6:
        print(f"Seu resultado do D100 é {random.randint(1, 100)}")
    else:
        print("ERROR")
        
    sleep(1.6)
    
    x = input("""\n===============================================================
    
DESEJA REINICIAR O PROGRAMA?
DIGITE [1] PARA NAO OU DIGITE QUALQUER TECLA PARA CONTINUAR: """)

"""i = "%.2f" % 3.141592653589793
print(i)"""   # Como limitar casas decimais 
    
