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

# Conversão de string para float, substituindo , por .
def converter(num_string):
    if ',' in num_string:
        return num_string.replace(',','.')
    return float(num_string)

# Verificador de números
def verifica_num(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

ini = input('DE: ').upper()
fim = input('PARA: ').upper()
valor = input('VALOR: ')

while verifica_num(valor) == False:
    print('Valor inválido!')
    valor = input('VALOR: ')
valor = converter(valor)


# CONVERSOR
if ini in ['C','F','K'] and fim in ['C','F','K']:
    # CELSIUS / KELVIN
    if ini == 'C' and fim == 'K':
        retorno = valor + 273
    if ini == 'K' and fim == 'C':
        retorno = valor - 273

    # CELSIUS / FAHRENHEIT
    if ini == 'C' and fim == 'F':
        retorno = (1.8 * valor) + 32
    if ini == 'F' and fim == 'C':
        retorno = (valor - 32) / 1.8

    # KELVIN / FAHRENHEIT
    if ini == 'F' and fim == 'K':
        retorno = ((valor - 32) * 5/9) + 273.15
    if ini == 'K' and fim == 'F':
        retorno = ((valor - 273.15) * 9/5) + 32
        
    print(retorno)
else:
    print('Unidade incorreta!')