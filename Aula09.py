import os
os.system('cls')


# try:
#     n = int(input('Informe um numero: '))
# except (ValueError, KeyboardInterrupt) as e:
#     print(f'Erro: {e}')


# except KeyboardInterrupt as e:
#     print('\nO usúario cancelou a operação...')
    

try:
    txt = input('Informe o nome:  ')[0]
except IndexError as e:
    print (f'{e} Precisa digitar algo: ')
else:
    print('Acertou')
finally:
    print('Sempre executado')

    



    
    



    




    


