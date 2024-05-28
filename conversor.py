# 2. Conversor de Temperatura
# Desenvolva um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
# Adicione uma interface de linha de comando para entrada de dados.

print('CONVERSOR DE UNIDADES DE TEMPERATURA')
print('')
print('Escalas disponíveis')
print('(C) Celsius')
print('(F) Fahrenheit')
print('(K) Kelvin')
print('')
print('>> Digite as letras correspondentes')

ini = input('DE: ')
fim = input('PARA: ')
valor = float(input('VALOR: '))

if ini in ['C','F','K'] and fim in ['C','F','K']:
    # CELSIUS / KELVIN
    if ini == 'C' and fim == 'K':
        retorno = valor + 273
    if ini == 'K' and fim == 'C':
        retorno = valor - 273

    # CELSIUS / FAHRENHEIT
    if ini == 'C' and fim == 'F':
        retorno = (1,8 * valor) + 32
    if ini == 'F' and fim == 'C':
        retorno = (valor - 32) / 1,8

    # KELVIN / FAHRENHEIT
    if ini == 'K' and fim == 'F':
        
        retorno = (1,8 * valor) + 32
        
    print(retorno)
else:
    print('Unidade incorreta!')