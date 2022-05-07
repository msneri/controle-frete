import cadastros

print(f'{"BEM - VINDO AO LOGISTIC":^40}')

retornar = 'SIM'
while retornar == 'SIM':
    print('-' * 40)
    print(f'{"MENU":^40}')
    print('-' * 40)
    print('1 - FAZER COTAÇÃO')
    print('2 - CADASTRAR TRANSPORTADORA')
    print('3 - CADASTRAR CLIENTE')
    print('4 - CONSULTAS')
    print('5 - SAIR')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        cadastros.cotacao()
    elif opcao == 2:
        cadastros.cadastroTrans()
    elif opcao == 3:
        cadastros.cadastroCliente()
    elif opcao == 4:
        cadastros.consulta()
    else:
        exit()


