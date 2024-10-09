import os
os.system('cls')


# try:
#     n = int(input('Informe um numero: '))
# except (ValueError, KeyboardInterrupt) as e:
#     print(f'Erro: {e}')


# except KeyboardInterrupt as e:
#     print('\nO usúario cancelou a operação...')
    

# try:
#     txt = input('Informe o nome:  ')[0]
# except IndexError as e:
#     print (f'{e} Precisa digitar algo: ')
# else:
#     print('Acertou')
# finally:
#     print('Sempre executado')




try:
    resp = input('Informe (s/n): ').lower()

    if resp == '':
        raise EOFError('Você não digitou nada')
    if  resp.isdigit():
        raise ValueError('Não infome números')
except EOFError as e:
    print(f'[{e}]')
except ValueError as e:
    print(f'[{e}]')


while True:
    try:
        num = int(input('Informe u número: '))
    except (ValueError) as e:
        print(f'{e} Valor informado não é válido')
    except KeyboardInterrupt as e:
        print(f'{e} Entrada interrompida pelo usuário')
        break
    else:
        print(f'{num} informado com sucesso')
        break

    





    
    



    




    


