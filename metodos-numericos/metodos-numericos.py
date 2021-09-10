import math


def f(x):
    return 3 * x - math.cos(x) + 2


def bissecao():
    xi = []
    i = 0
    erro = float(input('Digite o erro (epsilon): '))
    while True:
        a = float(input('Inicio do intervalo: '))
        b = float(input('Fim do intervalo: '))
        if f(a) * f(b) < 0:
            break
        else:
            print('\033[0:31mERRO! Não existe solução dentro desse intervalo.\033[m')
    while True:
        x = (a + b) / 2
        xi.append(x)
        if f(x) * f(a) < 0:
            b = x
        else:
            a = x
        i += 1
        if len(xi) > 1:
            if abs((xi[i - 1] - xi[i - 2])) < erro:
                break
    print(xi)
    return xi[-1]


#################################################################################


def fi(x):
    return - 1 - x * math.exp(x)


def aprox_suc():
    error_type = 0
    while error_type != 1 and error_type != 2:
        error_type = int(input('''[ 1 ] Erro Absoluto\n[ 2 ] Erro Relativo\nEscolha o tipo de erro: '''))
    i = 0
    xi = []
    erro = float(input('Digite o erro (epsilon): '))
    x0 = float(input('Solução inicial: '))
    while True:
        x = fi(x0)
        xi.append(x)
        i += 1
        if len(xi) > 1 and error_type == 1:
            if abs((xi[i - 1] - xi[i - 2])) < erro:
                break
        elif len(xi) > 1 and error_type == 2:
            if abs((xi[i - 1] - xi[i - 2]) / xi[i - 1]) < erro:
                break
        x0 = x
    print(xi)
    return xi[-1]


#################################################################################

def f1(x):
    return x * math.exp(x) - 7


def f_derivada(x):
    return math.exp(x) + x * math.exp(x)


def newton():
    xi = []
    i = 0
    erro = float(input('Digite o erro (epsilon): '))
    x0 = float(input('Qual o valor da aproximação inicial: '))
    while True:
        xi.append(x0)
        x = x0 - ((f1(x0)) / f_derivada(x0))
        if len(xi) > 1 and abs((xi[i - 1] - xi[i - 2])) < erro:
            break
        i += 1
        x0 = x
    print(xi)
    return xi[-1]


#print(f'{newton():.7f}')
#print(f'{bissecao():.7f}')
#print(f'{aprox_suc():.7f}')
