import os
os.system('cls')


try:
    n = int(input('Informe um numero: '))
except ValueError as e:
    print(f'{e}')
except KeyboardInterrupt as e:
    print('\nO usúario cancelou a operação...')



    


