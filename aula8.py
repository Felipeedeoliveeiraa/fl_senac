'''
numero = int(input("Digite um numero"))
divisores = 0
for divisor in range(1, numero):
    if numero % divisor == 0:
        divisores = divisores + 1
        if divisores > 1:
          break
if divisores > 1:
  print("não é primo")
else:
  print("é primo")
'''
  
'''
def identificar_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    invertido = texto[::-1]
    
    if texto == invertido:
        return True
    else:
        return False

entrada = input("Digite uma palavra, frase ou número: ")
if identificar_palindromo(entrada):
    print("A entrada é um palíndromo!")
else:
    print("A entrada não é um palíndromo!")
'''
'''
def menu_inicial():
    print('Programa para Conversão de Temperaturas')
    print('1. Converter de Celsius para Fahrenheit')
    print('2. Converter de Fahrenheit para Celsius')

def cel_fahr():
    C = float(input('Entre com a temperatura em graus Celsius: '))
    F = C * (9 / 5) + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))

def fahr_cel():
    F = float(input('Entre com a temperatura em graus Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(C))

if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        cel_fahr()

    if escolha == '2':
        fahr_cel()
'''
'''
ano = int(input('Digite o ano: '))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('É um ano bissexto')
else:
    print('Não é bissexto')
    '''
'''
def conta_vogais(string):
    string = string.lower() # para que a comparação não seja sensível a maiuscula/minuscula
    result = {}
    vogais = 'aeiou'
    for i in vogais:
        if i in string:
            result[i] = string.count(i)
    return result

string = input("Digite uma frase:")
contador_geral = conta_vogais (string)
print("a palavra", string, "contém", contador_geral, "vogais")                   
'''