transportadora = list()
clientes = list()


def cadastroCliente():

    print('-' * 40)
    print(f'{"MENU -> CASDASTRO CLIENTES":^40}')
    print('-' * 40)

    resp = 'SIM'
    while resp == 'SIM':
        clientes.append(str(input('Digite o nome do cliente: ')))
        resp = str(input('Deseja continuar cadastrando cliente? sim/não: ')).upper()
    retornar = str(input('Deseja retornar ao menu? SIM/NÃO: ')).upper()


def cadastroTrans():

    print('-' * 40)
    print(f'{"MENU -> CASDASTRO TRANSPORTADORA":^40}')
    print('-' * 40)

    resp = 'SIM'
    while resp == 'SIM':
            transportadora.append(str(input('Digite o nome da transportadora: ' )))
            resp = str(input('Deseja continuar cadastrando? sim/não: ')).upper()
    retornar = str(input('Deseja retornar ao menu? SIM/NÃO: ')).upper()


def cotacao():
    print('-' * 40)
    print(f'{"MENU -> COTAÇÕES":^40}')
    print('-' * 40)

    resp = 'SIM'
    while resp == 'SIM':
        valor_venda = float(input('Digite o valor da venda: '))
        valor_frete = float(input('Digite o valor do frete: '))
        media_entrega = valor_frete / valor_venda * 100
        print(f'A média do frete é: {media_entrega}')
        resp = str(input('Deseja continuar realizando cotação? sim/não: ')).upper()
    retornar = str(input('Deseja retornar ao menu? SIM/NÃO: ')).upper()


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
