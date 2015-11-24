# -*- encoding: utf-8 -*-

from mpi4py import MPI
from fibonacci import fibonacci

comm = MPI.COMM_WORLD
rank=comm.rank
size=comm.size
name=MPI.Get_processor_name()

if rank == 0:
    
    numero = 40
    comm.send(numero, dest=1, tag=1)

    total = comm.recv(source=1, tag=2)
    print total
    

if rank == 1:
    
    receive = comm.recv(source=0, tag=1)
    
    res = fibonacci(receive)
        
    comm.send(res, dest=0, tag=2)