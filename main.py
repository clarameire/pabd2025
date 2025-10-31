# # Programação com Acesso a Banco de Dados
# Revisão de Orientação a Objetos
# Prof. Guilherme Leal Santos

from empresa.config.database import SupabaseConnection
from empresa.dao.funcionario_dao import FuncionarioDAO

client = SupabaseConnection().client

# CRUD - Create, Read, Update, Delete

client = SupabaseConnection().client

# Criando DAO para acessar a tabela funcionario
funcionario_dao = FuncionarioDAO(client)

for funcionario in funcionario_dao.read_all():
    print(funcionario)




'''
from conta import Conta
from cliente import Cliente
from empresa.config.database import SupabaseConnection
from funcionario.controle_de_bonificacoes import ControleDeBonificacoes
# from funcionario.funcionario import Funcionario
from funcionario.gerente import Gerente
from ifrn.pessoa import Pessoa
from ifrn.funcionario import Funcionario

#Aula 17/10 - Polimorfismo, Classes Abstratas, Supabase

connection = SupabaseConnection()
client = connection.client

# pessoa = Pessoa('Guilherme', '111.222.333-44')
# print(pessoa)

# f = Funcionario('Guilherme', '111.222.333-44', '188651')
# print(f)


# f = Funcionario('Bartô Galeno', '111.222.333-44', 50000)
# print(f)
# print(f.get_bonificacao())
# g = Gerente('Reginaldo Rossi', '777.222.333-88', 250000, 1234, 10)
# print(g)
# print(g.get_bonificacao())

# controle = ControleDeBonificacoes()
# controle.registra(f)
# controle.registra(g)
# print(f'Total = R$ {controle.total:.2f}')



#Aula 10/10 - Métodos estáticos, métodos de classe
#Herança e reescrita de métodos

f = Funcionario('Bartô Galeno', '111.222.333-44', 50000)
print(f)
print(f.get_bonificacao())
g = Gerente('Reginaldo Rossi', '777.222.333-88', 250000, 1234, 10)
print(g)
print(g.get_bonificacao())

cliente1 = Cliente('Elvis Presley', '111.222.333-44')
conta1 = Conta(cliente1, 1, 123, 'elvis@gmail.com', 10000)
print(Conta.total_contas())

cliente2 = Cliente('Jonhny Cage', '222.333.444-55')
conta2 = Conta(cliente2, 2, 234, 'jonhny@outlook.com', 5000)
print(Conta.total_contas())

print(Conta.lista_contas())
print(Conta.get_saldo_total())

#Aula 26/09 - Agregação, Composição, Encapsulamento

cliente1 = Cliente('Elvis Presley', '111.222.333-44')
conta1 = Conta(cliente1, 1, 123, 'elvis@gmail.com', 10000)
conta1.extrato()
conta1.saca(500)
conta1.deposita(300)
conta1.saldo = 1

cliente2 = Cliente('Jonhny Cage', '222.333.444-55')
conta2 = Conta(cliente2, 2, 234, 'jonhny@outlook.com', 5000)
conta2.extrato()
conta2.saca(100)
conta2.deposita(600)
conta2.saldo = 1000000

conta1.transfere(conta2, 2000)
conta2.saca(10000)

conta1.historico.imprime()
conta2.historico.imprime()



#Aula 19/20 - Orientação a Objetos

from conta import Conta
from cliente import Cliente

cliente1 = Cliente('Elvis Presley', '111.222.333-44')
conta1 = Conta(cliente1, 1, 123, 'elvis@gmail.com', 12345678)
conta1.extrato()

cliente2 = Cliente('Jonhny Cage', '222.333.444-55')
conta2 = Conta(cliente2, 2, 234, 'jonhny@outlook.com', 23456789)
conta2.extrato()

if(conta2.transfere(conta1, 1000)):
    print('OK')
else:
    print('Ta Liso')
'''
'''
#Lista de palavras
frutas = ['Maçã', 'Banana', 'Laranja']
print(frutas)
print(frutas[0])
print(f'Tamanho: {len(frutas)}')

frutas.append('Uva') #adiciona no final
print(frutas)

frutas.insert(1, 'Abacaxi') #escolhe a posição ao adicionar
print(frutas)

# fruta = frutas.pop() -> remove o último elemento da lista
fruta = frutas.pop(0) # -> remove o elemento especificado
print(f'Removido: {fruta}')
print(frutas)

frutas.remove('Uva') #remove um elemento pelo nome
print(frutas)

#Lista de Números
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numeros)

numeros_ord_c = sorted(numeros)
print(f'Listan ordenada (c):{numeros_ord_c}')
numeros_ord_d = sorted(numeros, reverse=True)
print(f'Listan ordenada (d):{numeros_ord_d}')

#Dobrar números da lista
numeros_dobro = []
for n in numeros:
    numeros_dobro.append(n*2)
print(numeros_dobro)

numeros_dobro = list(map(lambda n: n*2, numeros))
print(numeros_dobro)

#Filtrar números da lista
numeros_filtrados = []
for n in numeros:
    if n > 4:
        numeros_filtrados.append(n)
print(numeros_filtrados)

numeros_filtro = list(filter(lambda n: n>4,numeros))
print(numeros_filtro)

#Reduz a lista a um único valor (soma)
from functools import reduce
soma = reduce(lambda soma, n: soma + n, numeros)
print(soma)
'''