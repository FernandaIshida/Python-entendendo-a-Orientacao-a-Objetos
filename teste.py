'''Estudo de programacao procedural e verificacao de fragil ligacao entre funcoes.
Mesma ideia sera trabalhada com OO a fim de efetuar melhorias.
'''
def cria_conta(numero, titular, saldo,limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta = [saldo] += valor

def saca(conta, valor):
    conta = [saldo] -= valor

def extrato(conta):
    print("Saldo {}".format(conta[saldo]))