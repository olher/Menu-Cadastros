from time import sleep
from Dados.menu import *


def cadastrar():
    nome = str(input('Digite o nome para cadastro:\n'))
    idade = int(input('Digite a idade:\n'))
    with open('Data.txt', 'a') as data:
        data.write(f'{nome}, {idade}\n')
    print(f'\33[32m{" CADASTRO FEITO ":=^50}\33[m')
    sleep(1)


def listar(voltar=True):
    with open('Data.txt', 'r') as data:
        print(f'{"POSIÇÃO":^10}{"NOME":<30}{"IDADE":^10}')
        for i, dado in enumerate(data.readlines()):
            dado = dado[:-1].split(', ')
            print(f'{i:^10}{dado[0]:<30}{dado[1]:^10}')
    if voltar:
        while True:
            voltar = str(input(f'{"="*50}\n{"[ENTER] MENU PRINCIPAL "}'))
            if voltar.strip() == '':
                break


def deletar():
    listar(voltar=False)
    i = n_cadastros()
    while True:
        try:
            deletar = int(input('Digite a Posição Para Deletar: '))
        except:
            print(f'\33[31m{" Digite Um Numero ":=^50}\33[m')
            sleep(1)
        else:
            if validador_de_input(deletar, 'posicao'):
                break
    print(f'\33[31m{" CONTATO DELETADO ":=^50}\33[m')
    sleep(1)

    with open('Data.txt', 'r') as data:
        lista = []
        for dados in data.readlines():
            linha = dados[:-1]
            lista.append(linha.split(', '))
    with open('Data.txt', 'w') as data:
        for i, dado in enumerate(lista):
            if i != deletar:
                data.write(f'{dado[0]}, {dado[1]}\n')


def buscar(itens=['pesquisa por posição',
           'pesquisa por nome',
           'pesquisa por idade']):

    while True:
        menu_buscar = menu(titulo='buscar contato', itens=itens, show_cadastro=False,
                           show_titulo=False, sair='VOLTAR')
        if menu_buscar == 1:
            with open('Data.txt', 'r') as data:
                while True:
                    try:
                        pesquisar = int(input('Digite a Posição Desejada: '))
                    except:
                        print(f'\33[31m{" POSIÇÃO INVALIDA ":=^50}\33[m')
                        sleep(1)
                    else:
                        if validador_de_input(pesquisar, 'posicao'):
                            break

                print(f'{"POSIÇÃO":^10}{"NOME":<30}{"IDADE":^10}')
                for i, dado in enumerate(data.readlines()):
                    if i == pesquisar:
                        dado = dado[:-1].split(', ')
                        print(f'{i:^10}{dado[0]:<30}{dado[1]:^10}')
                print('='*50)
                sleep(1)

        elif menu_buscar == 2:
            with open('Data.txt', 'r') as data:
                while True:
                    pesquisar = str(input('Digite o Nome Desejado: '))
                    if validador_de_input(pesquisar, 'nome'):
                        break

                print(f'{"POSIÇÃO":^10}{"NOME":<30}{"IDADE":^10}')
                for i, dado in enumerate(data.readlines()):
                    dado = dado[:-1].split(', ')
                    if pesquisar.upper().strip() == dado[0].upper().strip():
                        print(f'{i:^10}{dado[0]:<30}{dado[1]:^10}')
                print('='*50)
                sleep(1)

        elif menu_buscar == 3:
            with open('Data.txt', 'r') as data:
                while True:
                    try:
                        pesquisar = int(input('Digite a Idade Desejada: '))
                    except:
                        print(f'\33[31m{" IDADE INVÁLIDA ":=^50}\33[m')
                        sleep(1)
                    else:
                        if validador_de_input(pesquisar, 'idade'):
                            break

                print(f'{"POSIÇÃO":^10}{"NOME":<30}{"IDADE":^10}')
                for i, dado in enumerate(data.readlines()):
                    dado = dado[:-1].split(', ')
                    if pesquisar == int(dado[1]):
                        print(f'{i:^10}{dado[0]:<30}{dado[1]:^10}')
                print('='*50)
                sleep(1)

        elif menu_buscar == 'sair':
            break


def atualizar():
    listar(voltar=False)
    print('='*50)
    while True:
        try:
            atualizar = int(input('Digite a Posição Para Atualizar: '))
        except:
            print(f'\33[31m{" POSIÇÃO INVÁLIDA ":=^50}\33[m')
            sleep(1)
        else:
            if validador_de_input(atualizar, 'posicao'):
                break

    nome_atualizado = str(input('Digite Novo Nome: '))
    idade_atualizada = int(input('Digite Nova Idade: '))
    lista = []
    with open('Data.txt', 'r') as data:
        for dados in data.readlines():
            dados = dados[:-1]
            lista.append(dados.split(', '))
    with open('Data.txt', 'w') as data:
        for i, dados in enumerate(lista):
            if i != atualizar:
                data.write(f'{dados[0]}, {dados[1]}\n')
            else:
                data.write(f'{nome_atualizado}, {idade_atualizada}\n')
    print(f'\33[32m{" LISTA ATUALIZADA ":=^50}\33[m')
    sleep(1)



def n_cadastros():
    with open('Data.txt', 'r') as data:
        return (len(data.readlines()))


def validador_de_input(valor, modo):
    i = n_cadastros()
    if modo == 'posicao':
        if valor in list(range(i)):
            return True
        else:
            print(f'\33[31m{" POSIÇÃO INVÁLIDA ":=^50}\33[m')
    else:
        with open('Data.txt', 'r') as data:
            lista = []
            lis_nomes = []
            lis_idades = []
            for dados in data.readlines():
                dados = dados[:-1]
                lista.append(dados.split(', '))
            for nome, idade in lista:
                lis_nomes.append(nome)
                lis_idades.append(int(idade))

            if modo == 'nome':
                if valor in lis_nomes:
                    return True
                else:
                    print(f'\33[31m{" NOME INVÁLIDO ":=^50}\33[m')

            if modo == 'idade':
                if valor in lis_idades:
                    return True
                else:
                    print(f'\33[31m{" IDADE INVÁLIDA ":=^50}\33[m')