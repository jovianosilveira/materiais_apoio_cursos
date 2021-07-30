import time

print('iniciando o código')

segundos = 5
for i in range (segundos):
    print("Aguarde",segundos - i,"segundos")
    time.sleep(1)

# Entrada de informações
b = float(input('digite a largura: '))
h = float(input('digite a altura: '))
print("OK, vou calcular para você!\nAguarde 5 segundos")
time.sleep(5)

# Calculos
x = b*h
mensagem = 'a metragem quadrada é: ' + str(x)

# Retorno usuário
print(mensagem)