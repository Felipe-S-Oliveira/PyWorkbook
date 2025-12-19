
'''
================================================
===========   REGISTRO DE FUNÇÕES     ==========
================================================
'''

import os
import platform

_dict_func = {}

def regFunction(title):
    
    def wrapper(func):
        _dict_func[title] = func
        return func
    return wrapper


'''
==================================
===========   GERAL     ==========
==================================
'''

def clearTerminal():
    
    OS = platform.system
    if OS == "Windows":
        os.system('cls')
    else:
        os.system('clear')


'''
========================================
===========   INICIA MENU     ==========
========================================
'''

def startMenu():

    clearTerminal()

    while True:
        
        print('\n-------- MENU DE FUNÇÕES --------')
        print('=================================\n')

        menuOptions = list(_dict_func.keys())

        for index, option in enumerate(menuOptions):
            print(f' [{index + 1}] - {menuOptions[index]}')

        print('---------------------------------')
        print('\n [0] - Sair')

        selection = int(input('\nDigite o número da função desejada: '))
        
        if selection == 0:
            print('\nSaindo...\n')
            break
        else:
            titleSelected = menuOptions[selection - 1]
            functionToRun = _dict_func[titleSelected]

            print(f'\nRodando a função {titleSelected}:\n')

            functionToRun()
