# Hannah Spencer
# spehan01
# Lab 3

n = 10  
series = 'sum'
series = 'fibonacci'
fib = 0 
a = 1
b = 0
i = 0

if series == 'fibonacci':
    while i < n:
        fib = a + b
        a = b
        b = fib
        i = i + 1
    print fib
   
elif series == 'sum':
    while i < n:
        b = b + 3
        i = i + 1
    print b
            
else: 
    print 'invalid string'
