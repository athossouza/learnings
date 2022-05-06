def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print('O saldo é {}'.format(conta['saldo']))


comp = len('Pedir o ID e senha do acesso que o cliente já tem instalado')
print(comp)