# -*- encoding: utf-8 -*-

from mpi4py import MPI
from fibonacci import fibonacci
import time

ini = time.time()

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

numero = 10
lista_sequencia = []
soma = 0

if rank == 0:
    
    for i in range(numero):
        lista_sequencia.append(i)
    data = lista_sequencia
    
    chunks = [[] for i in range(size)]
    
    for i, chunk in enumerate(data):
        chunks[i % size].append(chunk)
    print 'Lista que será processada:',chunks
else:
    data = None
    chunks = None
   
data = comm.scatter(chunks, root=0)

for i in data:
    if type(i) == list:
        res = fibonacci(i)
    else:
        res = fibonacci(i)
    data = res
    print 'Processo',rank,'tem dado:',data

    newData = comm.gather(data,root=0)

if rank == 0:
    print 'Processo mestre dado:',newData
    print "Soma total :", sum(newData)

    fim = time.time()
    print "Tempo total de execução: ", fim-ini



