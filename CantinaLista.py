#FilaCantina

clientes = []
prod = []

for i in range(7):
    nome = input('Forneça seu nome: ')
    produto = input('Insira o produto desejado: ')
    clientes.append(nome)
    prod.append(produto)
print('Clientes ------- Produto')
n = 0
while n<=7:
    print(clientes[n],'-------', prod[n])
    n = n+1

