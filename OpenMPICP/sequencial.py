from fibonacci import fibonacci
numero = 40
res = 0
lista_sequencia = []
lista_sequencia_fib = []

for i in range(1, numero+1):
    lista_sequencia.append(i)
print "Sequencia a ser processada: " + str(lista_sequencia)

indice = 0

for i in lista_sequencia:
    lista_sequencia_fib.append(fibonacci(i))
    print " %d " %lista_sequencia_fib[indice]
    indice += 1

print "Lista fibonacci: ", lista_sequencia_fib
    
print "Soma total: ", sum(lista_sequencia_fib)
