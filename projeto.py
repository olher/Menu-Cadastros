from Dados.menu import *
from Dados.funcoes import *
from time import sleep

itens=['CADASTRAR CONTATO', 'LISTAR CONTATO', 'DELETAR CONTATO',
       'BUSCAR CONTATO', 'ATUALIZAR CONTATO']

while True:
    n_cad = n_cadastros()
    menu_principal = menu(titulo='Base de cadastros', itens=itens, n_cadastros=n_cad)

    if menu_principal == 1:
        cadastrar()
    elif menu_principal == 2:
        listar()
    elif menu_principal == 3:
        deletar()
    elif menu_principal == 4:
        buscar()
    elif menu_principal == 5:
        atualizar()
    elif menu_principal == 'sair':
        print(f'{" SAINDO ":=^50}')
        break
    else:
        print(f'\33[31m{" DIGITE UMA OPÇÃO VALIDA ":=^50}\33[m')
        sleep(3)
