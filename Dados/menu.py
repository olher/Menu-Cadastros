from time import sleep

def menu (titulo='PROJETO MENU PYTHON',
          itens=['CADASTRAR CONTATO', 'LISTAR CONTATO',
                 'DELETAR CONTATO', 'BUSCAR CONTATO',
                 'ATUALIZAR CONTATO'],
          show_cadastro=True,
          n_cadastros=0,
          show_titulo=True,
          sair='SAIR'):

    if show_titulo:
        tam = 50 - 16 - len(str(n_cadastros))
        print('=' * 50)
        print(f'\33[1m{titulo.upper():^50}\33[m')
        print('=' * 50)

    if show_cadastro:
        print('\33[1mMENU:', end='')
        print(f'{n_cadastros:>{tam}} CADASTRO(S)\33[m')
    else:
        print('\33[1mMENU:\33[m')

    for i, item in enumerate(itens):
        print(f'\33[1m[{i+1}]\33[m {item.upper()}')
    print(f'\33[1m[ENTER]\33[m {sair.upper()}')
    print('=' * 50)

    while True:
        n = input('Digite a Opção Desejada: ').strip()
        if n == '':
            return 'sair'
            break
        else:
            try:
                print(f'{" " + itens[int(n) - 1].upper() + " ":=^50}')
            except:
                print(f'\33[31m{" DIGITE UMA OPÇÃO VALIDA ":=^50}\33[m')
                sleep(1)
            else:
                return int(n)
                break
