transportadora = list()
clientes = list()

def consulta():
    print('-' * 40)
    print(f'{"MENU -> CONSULTAS":^40}')
    print('-' * 40)
    print('1 - LISTAR TRANSPORTADORAS')
    print('2 - LISTAR CLIENTES')

    opcao_listagem = int(input('Digite a opção: '))
    if opcao_listagem == 1:
        for i, c in enumerate(transportadora):
            print(f'{i+1} - {c}')
    elif opcao_listagem == 2:
        for i, c in enumerate(clientes):
            print(f'{i+1} - {c}')
    retornar = str(input('Deseja retornar ao menu? SIM/NÃO: ')).upper()