# -*- encoding: utf-8 -*-

from mpi4py import MPI
from fibonacci import fibonacci
import time

ini = time.time()

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
    
    chunks = [[] for i in range(size)]
    
    for i, chunk in enumerate(data):
        chunks[i % size].append(chunk)
    print 'Lista que será processada:',data
else:
    data = None
    chunks = None
   
data = comm.scatter(chunks, root=0)

for i in range(len(data)):
    if type(data) == list:
        res = fibonacci(data[i])
    else:
        res = fibonacci(data)
    data = res
    print 'Processo',rank,'tem dado:',res

newData = comm.gather(data,root=0)

if rank == 0:
    print 'Processo mestre dado:',newData
    #print "Soma total :", sum(newData)

    fim = time.time()
    print "Tempo total de execução: ", fim-ini



