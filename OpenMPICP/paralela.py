# -*- encoding: utf-8 -*-

from mpi4py import MPI
from fibonacci import fibonacci

comm = MPI.COMM_WORLD
rank=comm.rank
size=comm.size
name=MPI.Get_processor_name()

numero = 4
total = 0

if rank == 0:
    comm.send(1, dest=1, tag=1)
    total = total + comm.recv(source=1, tag=4)

for i in range(1, numero):
    if rank == i:
        receive = comm.recv(source=i-1, tag=i)
        res = fibonacci(receive)
        comm.send(res, dest=0, tag=i)
print total
