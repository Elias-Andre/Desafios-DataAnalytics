valor = float(input())

if valor > 0:
    print('Deposito realizado com sucesso!\n Saldo atual: R$ '"%.2f" % valor)
elif valor < 0:
   print('Valor invalido! Digite um valor maior que zero.')
else:
   print('Encerrando o programa...')