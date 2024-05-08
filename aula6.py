'''
def fatorial (a) :
    if a == 0:
        return 1 
    else :
        fat = 1
    for i in range (1,  a+1):
        fat *= i 
    return fat

x = int(input("digite um número inteiro"))
print("o fatorial de", x, "é" , fatorial(x))
'''
'''
nome = (input("digite seu nome"))
idade = int(input("digite sua idade"))
altura = float(input("digite sua altura"))
print (nome)
print (idade)
print ("sua altura é:" ,nome,)
print ("sua altura é:" ,idade,)
print ("sua altura é:" ,altura,)
'''
'''def contagem_regressiva():
    numero = int(input("digite um número inteiro positivo"))

    if numero <= 0 :
     print("por favor, digite um número inteiro positivo.")
     contagem_regressiva()
    else:
       while numero >= 0:
        print(numero)
        numero -= 1
contagem_regressiva() 
'''
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
 