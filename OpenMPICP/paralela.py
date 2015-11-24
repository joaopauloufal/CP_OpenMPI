# -*- encoding: utf-8 -*-

from mpi4py import MPI
from fibonacci import fibonacci

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

numero = 40
lista_sequencia = []
soma = 0

if rank == 0:
    for i in range(1, numero+1):
        lista_sequencia.append(i)
    data = lista_sequencia
    print 'Lista que será processada:',data
else:
    data = None
   
data = comm.scatter(data, root=0)
res = fibonacci(data)
data = res
print 'Processo',rank,'tem dado:',data

newData = comm.gather(data,root=0)

if rank == 0:
    print 'Processo mestre dado:',newData
    print "Soma total :", sum(newData)



