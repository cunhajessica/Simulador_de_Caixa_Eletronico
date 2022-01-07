#simulador de caixa eletrônico
print('='*30)
print('{:^30}'.format('BANCO TIO PATINHAS'))
print('='*30)
num = int(input('Qual valor você quer sacar? R$ '))
total = num
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} notas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('Use seu dinheiro com sabedoria. :) Volte sempre!')

