from fibonacci import fibonacci
numero = 40
res = 0

for i in range(1, numero):
    fibonacci_numero = fibonacci(i)
    print " %d " %fibonacci_numero
    res = res + fibonacci_numero
    
print "Soma total: %d" %res
